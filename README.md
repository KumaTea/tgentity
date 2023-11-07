# TgEntity

Convert Telegram entities to HTML or Markdown.

This project is a rewrite of
[@telegraf/entity](https://github.com/telegraf/entity)
in Python.

`pip install tgentity`

### Usage

```python
from tgentity import to_markdown_v2, to_html

html = to_html(message)
markdown = to_markdown_v2(message)
```

* Aliases
  * `to_md` = `to_markdown_v2`
  * `to_markdown` = `to_markdown_v2`
