from tgentity.types import Node


def HTML(to_match: str, node: Node = None) -> str:
    node_type = str(node.type).lower()
    if node_type == "bold":
        return f"<b>{to_match}</b>"
    if node_type == "italic":
        return f"<i>{to_match}</i>"
    if node_type == "underline":
        return f"<u>{to_match}</u>"
    if node_type == "strikethrough":
        return f"<del>{to_match}</del>"
    if node_type == "code":
        return f"<code>{to_match}</code>"
    if node_type == "pre":
        if node.language:
            return f"<pre><code class=\"language-{node.language}\">{to_match}</code></pre>"
        return f"<pre>{to_match}</pre>"
    if node_type == "spoiler":
        return f"<span class=\"tg-spoiler\">{to_match}</span>"
    if node_type == "url":
        return f"<a href=\"{node.text}\">{to_match}</a>"
    if node_type == "text_link":
        return f"<a href=\"{node.url}\">{to_match}</a>"
    if node_type == "text_mention":
        return f"<a href=\"tg://user?id={node.user.id}\">{to_match}</a>"
    if (
        node_type == "mention" or
        node_type == "custom_emoji" or
        node_type == "hashtag" or
        node_type == "cashtag" or
        node_type == "bot_command" or
        node_type == "phone_number" or
        node_type == "email"
    ):
        return to_match
    return to_match


def MarkdownV2(to_match: str, node: Node = None) -> str:
    node_type = str(node.type).lower()
    if node_type == "bold":
        return f"*{to_match}*"
    if node_type == "italic":
        return f"_{to_match}_"
    if node_type == "underline":
        return f"__{to_match}__"
    if node_type == "strikethrough":
        return f"~{to_match}~"
    if node_type == "code":
        return f"`{to_match}`"
    if node_type == "pre":
        if node.language:
            return f"```{node.language}\n{to_match}\n```"
        return f"```\n{to_match}\n```"
    if node_type == "spoiler":
        return f"||{to_match}||"
    if node_type == "url":
        return to_match
    if node_type == "text_link":
        return f"[{to_match}]({node.url})"
    if node_type == "text_mention":
        return f"[{to_match}](tg://user?id={node.user.id})"
    if (
            node_type == "mention" or
            node_type == "custom_emoji" or
            node_type == "hashtag" or
            node_type == "cashtag" or
            node_type == "bot_command" or
            node_type == "phone_number" or
            node_type == "email"
    ):
        return to_match
    return to_match
