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
    from telethon.types import Message, MessageEntity
    imported = True
except ImportError:
    pass

# aiogram
try:
    from aiogram.types import Message, MessageEntity
    imported = True
except ImportError:
    pass

# pyTelegramBotAPI
try:
    from telebot.types import Message, MessageEntity
    imported = True
except ImportError:
    pass

# simple
if not imported:
    class MessageEntity:
        def __init__(
                self,
                type: str,
                offset: int,
                length: int,
        ):
            self.type = type
            self.offset = offset
            self.length = length


    class Message:
        def __init__(
                self,
                id: int,
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
