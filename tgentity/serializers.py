from tgentity.types import Node


def HTML(to_match: str, node: Node = None) -> str:
    node_type = str(node.type).lower()
    if "bold" in node_type:
        return f"<b>{to_match}</b>"
    if "italic" in node_type:
        return f"<i>{to_match}</i>"
    if "underline" in node_type:
        return f"<u>{to_match}</u>"
    if "strikethrough" in node_type:
        return f"<del>{to_match}</del>"
    if "code" in node_type:
        return f"<code>{to_match}</code>"
    if "pre" in node_type:
        if node.language:
            return f"<pre><code class=\"language-{node.language}\">{to_match}</code></pre>"
        return f"<pre>{to_match}</pre>"
    if "spoiler" in node_type:
        return f"<span class=\"tg-spoiler\">{to_match}</span>"
    if "url" in node_type:
        return f"<a href=\"{node.text}\">{to_match}</a>"
    if "text_link" in node_type:
        return f"<a href=\"{node.url}\">{to_match}</a>"
    if "text_mention" in node_type:
        return f"<a href=\"tg://user?id={node.user.id}\">{to_match}</a>"
    if (
        "mention" in node_type or
        "custom_emoji" in node_type or
        "hashtag" in node_type or
        "cashtag" in node_type or
        "bot_command" in node_type or
        "phone_number" in node_type or
        "email" in node_type
    ):
        return to_match
    return to_match


def MarkdownV2(to_match: str, node: Node = None) -> str:
    node_type = str(node.type).lower()
    if "bold" in node_type:
        return f"*{to_match}*"
    if "italic" in node_type:
        return f"_{to_match}_"
    if "underline" in node_type:
        return f"__{to_match}__"
    if "strikethrough" in node_type:
        return f"~{to_match}~"
    if "code" in node_type:
        return f"`{to_match}`"
    if "pre" in node_type:
        if node.language:
            return f"```{node.language}\n{to_match}\n```"
        return f"```\n{to_match}\n```"
    if "spoiler" in node_type:
        return f"||{to_match}||"
    if "url" in node_type:
        return to_match
    if "text_link" in node_type:
        return f"[{to_match}]({node.url})"
    if "text_mention" in node_type:
        return f"[{to_match}](tg://user?id={node.user.id})"
    if (
        "mention" in node_type or
        "custom_emoji" in node_type or
        "hashtag" in node_type or
        "cashtag" in node_type or
        "bot_command" in node_type or
        "phone_number" in node_type or
        "email" in node_type
    ):
        return to_match
    return to_match
