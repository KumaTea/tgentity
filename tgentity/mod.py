from typing import List
import tgentity.escapers as escapers
import tgentity.serializers as serializers
from tgentity.types import Message, MessageEntity, Tree, Node


# https://github.com/tdlib/td/blob/d79bd4b69403868897496da39b773ab25c69f6af/td/telegram/MessageEntity.cpp#L39
def type_priority(entity_type: str) -> int:
    entity_type = str(entity_type).lower()
    if "mention"       in entity_type: return 50
    if "hashtag"       in entity_type: return 50
    if "bot_command"   in entity_type: return 50
    if "url"           in entity_type: return 50
    if "email"         in entity_type: return 50
    if "bold"          in entity_type: return 90
    if "italic"        in entity_type: return 91
    if "code"          in entity_type: return 20
    if "pre"           in entity_type: return 11
    if "text_link"     in entity_type: return 49
    if "text_mention"  in entity_type: return 49
    if "cashtag"       in entity_type: return 50
    if "phone_number"  in entity_type: return 50
    if "underline"     in entity_type: return 92
    if "strikethrough" in entity_type: return 93
    if "blockquote"    in entity_type: return 0
    if "spoiler"       in entity_type: return 94
    if "custom_emoji"  in entity_type: return 99


def find_children(from_entity_index: int, parent: MessageEntity, entities: List[MessageEntity]) -> List[MessageEntity]:
    ret: List[MessageEntity] = []

    for i in range(from_entity_index + 1, len(entities)):
        entity = entities[i]
        if entity.offset + entity.length > parent.offset + parent.length:
            break
        ret.append(entity)

    return ret


def ends(entity: MessageEntity) -> int:
    return entity.offset + entity.length


def to_tree(msg: Message, offset: int = 0, upto: int = float("inf")) -> Tree:
    if not msg.entities:
        return [msg.text[offset:upto]]

    nodes: Tree = []
    last = offset
    i = 0

    while i < len(msg.entities):
        entity = msg.entities[i]

        # there's some text that isn't in an entity
        if last < entity.offset:
            nodes.append(msg.text[last:entity.offset])
            last = entity.offset

        children = find_children(i, entity, msg.entities)
        node = Node(**entity.__dict__)
        node.text = msg.text[entity.offset:ends(entity)]
        node.children = to_tree(Message(id=msg.id, text=msg.text, entities=children), entity.offset, ends(entity))

        last = ends(node)

        nodes.append(node)
        i += len(children) + 1

    if last < upto:
        final = msg.text[last:]
        if final:
            nodes.append(final)

    return nodes


def serialize(tree: Tree, serializer: serializers.HTML, escaper: escapers.HTML) -> str:
    ret = ""
    for node in tree:
        if isinstance(node, str):
            ret += escaper(node)
        else:
            ret += serializer(serialize(node.children, serializer, escaper), node)
    return ret


def serialise_with(serializer: serializers.HTML, escaper: escapers.HTML):
    def inner(message: Message) -> str:
        if not message.text:
            message.text = message.caption
            message.entities = message.caption_entities
        if not message.entities:
            return serializer(message.text)

        # def entities_sort(a, b):
        #     if a.offset < b.offset: return -1
        #     if a.offset > b.offset: return 1
        #     if a.length > b.length: return -1
        #     if a.length < b.length: return 1
        #     a_priority = type_priority(a.type)
        #     b_priority = type_priority(b.type)
        #     if a_priority < b_priority: return -1
        #     if a_priority > b_priority: return 1
        #     return 0

        message.entities = sorted(message.entities, key=lambda x: (x.offset, -x.length, type_priority(x.type)))

        return serialize(to_tree(message), serializer, escaper)
    return inner


to_html = serialise_with(serializers.HTML, escapers.HTML)
to_markdown_v2 = serialise_with(serializers.MarkdownV2, escapers.MarkdownV2)

# export the following names
__all__ = ["serializers", "escapers", "serialise_with", "to_html", "to_markdown_v2"]
