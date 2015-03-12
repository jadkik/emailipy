# emailipy

A small library for inlining css into html and checking the css for email incompatibilities. Also included are two small command line utilities.

```
import emailipy

html = u'<div class="test">stuff</div>'
css = ".test { font-size: 14px; }"

emailipy.inline_css(html, css)
>>> u'<div class="test" style="font-size:14px;"">stuff</div>'
```

By default the `inline_css` function will strip out css that will not work on all email clients. You can allow all css to slip through with the `include_invalid` flag.

You can also use the css lint function on its own.

```
import emailipy

css = ".test { opacity: 0.8; }"

emailipy.lint_css(css)
>>> ['Invalid Rule: .test { opacity: 0.8; } -- Outlook 2007/10/13 | Outlook 03/Express/Mail | Yahoo! Mail | Google Gmail']
```

## emailipy-lint

A command line utility for checking css for email incompatibilities.

```
$ emailipy-lint
emailipy-lint <css_file>

$ emailipy-lint test.css
Invalid Rule: h1 { opacity: 0.8; } -- Outlook 2007/10/13 | Outlook 03/Express/Mail | Yahoo! Mail | Google Gmail
Invalid Rule: div { margin: 12px; } -- Outlook.com
Invalid Rule: .subtext { background: #FF00FF; } -- Outlook 2007/10/13 | Outlook 03/Express/Mail | Outlook.com | Yahoo! Mail | Google Gmail
Invalid Rule: div.subtext ~ div { margin: 18px; } -- Outlook.com
```

## emailipy-inline

A command line utility for inlining css in an html file. Allows you to disable the linter.

```
$ emailipy-inline
emailipy-inline <html_file> <css_file>
    --allow_invalid_css     Allows css that doesn't lint.
```