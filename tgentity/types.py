from typing import List, Union

imported = False

# pyrogram
try:
    from pyrogram.types import Message, MessageEntity

    imported = True
except ImportError:
    pass

# python-telegram-bot
try:
    from telegram import Message, MessageEntity

    imported = True
except ImportError:
    pass

# telethon
try:
    from telethon.tl.custom import Message, MessageEntity

    imported = True
except ImportError:
    pass

# simple
if not imported:
    class MessageEntity:
        def __init__(
                self,
                type: str = None,
                offset: int = None,
                length: int = None,
                url: str = None,
                user=None,
                language: str = None,
                custom_emoji_id: int = None
        ):
            self.type = type
            self.offset = offset
            self.length = length
            self.url = url
            self.user = user
            self.language = language
            self.custom_emoji_id = custom_emoji_id


    class Message:
        def __init__(
                self,
                id: int = None,
                text: str = None,
                caption: str = None,
                entities: List[MessageEntity] = None,
                caption_entities: List[MessageEntity] = None
        ):
            self.id = id
            self.text = text
            self.caption = caption
            self.entities = entities
            self.caption_entities = caption_entities


    imported = True


Leaf = str


class Node(MessageEntity):
    def __init__(
            self,
            type: str,
            offset: int,
            length: int,
            text: str = None,
            children: List[Union[MessageEntity, Leaf]] = None,
            **kwargs
    ):
        super().__init__(type=type, offset=offset, length=length)
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.text = text
        self.children = children


Tree = List[Union[Node, Leaf]]
