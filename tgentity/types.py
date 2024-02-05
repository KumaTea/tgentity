import importlib
from typing import List, Union


imported = None
APIs = [
    'pyrogram.types',  # pyrogram
    'telegram',  # python-telegram-bot
    'telethon.types',  # telethon
    'aiogram.types',  # aiogram
    'telebot.types'  # pyTelegramBotAPI
]

for name in APIs:
    try:
        api = importlib.import_module(name)
        Message = api.Message
        MessageEntity = api.MessageEntity
        imported = name
        break
    except ImportError:
        pass
    except AttributeError:
        pass

# simple
if not imported:
    class MessageEntity:
        def __init__(
                self,
                type: str,
                offset: int,
                length: int,
                **kwargs
        ):
            self.type = type
            self.offset = offset
            self.length = length
            for key, value in kwargs.items():
                setattr(self, key, value)

    class Message:
        def __init__(
                self,
                id: int,
                text: str = None,
                caption: str = None,
                entities: List[MessageEntity] = None,
                caption_entities: List[MessageEntity] = None,
                **kwargs
        ):
            self.id = id
            self.text = text
            self.caption = caption
            self.entities = entities
            self.caption_entities = caption_entities
            for key, value in kwargs.items():
                setattr(self, key, value)


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
