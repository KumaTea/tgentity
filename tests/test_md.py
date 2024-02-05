import unittest
from tgentity import to_markdown_v2
from tgentity.types import Message, MessageEntity


MarkdownV2_test = "URL entity inside bold must stringify to Markdown correctly"


class TestMarkdownV2(unittest.TestCase):
    print("Testing Markdown V2")
    print(f"API: \n  {Message=}\n  {MessageEntity=}\n\n")

    def test_markdown_v2(self):
        assert to_markdown_v2(
            Message(
                id=0,
                text="Hello, https://feathers.studio!",
                entities=[
                    MessageEntity(type="bold", offset=0, length=len("Hello, https://feathers.studio!")),
                    MessageEntity(type="url", offset=len("Hello, "), length=len("https://feathers.studio")),
                ]
            )
        ) == "*Hello, https://feathers\\.studio\\!*", MarkdownV2_test

        assert to_markdown_v2(
            Message(
                id=0,
                text="Hello, feathers.studio!",
                entities=[
                    MessageEntity(type="bold", offset=0, length=len("Hello, feathers.studio!")),
                    MessageEntity(
                        type="text_link",
                        offset=len("Hello, "),
                        length=len("feathers.studio"),
                        url="https://feathers.studio"),
                ]
            )
        ) == "*Hello, [feathers\\.studio](https://feathers.studio)\\!*", MarkdownV2_test

        assert to_markdown_v2(
            Message(
                id=0,
                text="👉 Link :- https://example.com",
                entities=[
                    MessageEntity(type="bold", offset=0, length=10),
                    MessageEntity(type="url", offset=10, length=19),
                    MessageEntity(type="bold", offset=10, length=19),
                ]
            )
        ) == "*👉 Link :\\- **https://example\\.com*", MarkdownV2_test


if __name__ == "__main__":
    unittest.main()
