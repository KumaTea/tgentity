from tgentity.types import Node


def HTML(match: str, node: Node = None) -> str:
    match node.type:
        case "bold":
            return f"<b>{match}</b>"
        case "italic":
            return f"<i>{match}</i>"
        case "underline":
            return f"<u>{match}</u>"
        case "strikethrough":
            return f"<del>{match}</del>"
        case "code":
            return f"<code>{match}</code>"
        case "pre":
            if node.language:
                return f"<pre><code class=\"language-{node.language}\">{match}</code></pre>"
            return f"<pre>{match}</pre>"
        case "spoiler":
            return f"<span class=\"tg-spoiler\">{match}</span>"
        case "url":
            return f"<a href=\"{node.text}\">{match}</a>"
        case "text_link":
            return f"<a href=\"{node.url}\">{match}</a>"
        case "text_mention":
            return f"<a href=\"tg://user?id={node.user.id}\">{match}</a>"
        case "mention", "custom_emoji", "hashtag", "cashtag", "bot_command", "phone_number", "email", _:
            return match


def MarkdownV2(match: str, node: Node = None) -> str:
    match node.type:
        case "bold":
            return f"*{match}*"
        case "italic":
            return f"_{match}_"
        case "underline":
            return f"__{match}__"
        case "strikethrough":
            return f"~{match}~"
        case "code":
            return f"`{match}`"
        case "pre":
            if node.language:
                return f"```{node.language}\n{match}\n```"
            return f"```\n{match}\n```"
        case "spoiler":
            return f"||{match}||"
        case "url":
            return match
        case "text_link":
            return f"[{match}]({node.url})"
        case "text_mention":
            return f"[{match}](tg://user?id={node.user.id})"
        case "mention", "custom_emoji", "hashtag", "cashtag", "bot_command", "phone_number", "email", _:
            return match
