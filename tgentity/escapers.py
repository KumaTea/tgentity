# escapeHTML borrowed from https://github.com/feathers-studio/hyperactive/blob/bbd67beace6744c4b8b48637a96c2daed416ebde/hyper/util.py


def HTML(s: str) -> str:
    escapables = {
        "<": "&lt;",
        ">": "&gt;",
        "&": "&amp;",
    }

    return "".join(escapables.get(c, c) for c in s)


def MarkdownV2(s: str) -> str:
    escapables = {
        "_": "\\_",
        "*": "\\*",
        "[": "\\[",
        "]": "\\]",
        "(": "\\(",
        ")": "\\)",
        "~": "\\~",
        "`": "\\`",
        ">": "\\>",
        "#": "\\#",
        "+": "\\+",
        "-": "\\-",
        "=": "\\=",
        "|": "\\|",
        "{": "\\{",
        "}": "\\}",
        ".": "\\.",
        "!": "\\!",
    }

    return "".join(escapables.get(c, c) for c in s)
