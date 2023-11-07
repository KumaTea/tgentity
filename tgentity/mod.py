from typing import List
import tgentity.escapers as escapers
import tgentity.serializers as serializers
from tgentity.types import Message, MessageEntity, Tree, Node


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

        message.entities = sorted(message.entities, key=lambda e: (e.offset, -e.length))

        return serialize(to_tree(message), serializer, escaper)
    return inner


to_html = serialise_with(serializers.HTML, escapers.HTML)
to_markdown_v2 = serialise_with(serializers.MarkdownV2, escapers.MarkdownV2)

# export the following names
__all__ = ["serializers", "escapers", "serialise_with", "to_html", "to_markdown_v2"]
