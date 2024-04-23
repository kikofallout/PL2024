import re

# Define a dictionary to map regex patterns to HTML tags
patterns = {
    re.compile("^\\#[^#].*$"): ("<h1>", "</h1>"),
    re.compile("^\\#{2}[^#].*$"): ("<h2>", "</h2>"),
    re.compile("^\\#{3}[^#].*$"): ("<h3>", "</h3>"),
    re.compile("^\\*{2}[^\\*].*\\*{2}$"): ("<b>", "</b>"),
    re.compile("^\\*[^\\*].*\\*$"): ("<i>", "</i>"),
    re.compile("^>.*$"): ("<blockquote>", "</blockquote>"),
    re.compile("^\\d\\..*$"): ("<ol><li>", "</li></ol>"),
    re.compile("^-[^-].*$"): ("<ul><li>", "</li></ul>"),
    re.compile("^`[^`].*[^`]`$"): ("<code>", "</code>"),
    re.compile("^\\[\\w*\\]\\([\\w\\:/.]*\\)$"): ("<a href=\"", "\">link</a>"),
    re.compile("^!\\[[^\\]]*\\]\\(\\.{2}/[^\\)]*\\)$"): ("<img src=\"", "\" alt=\"image\"/>"),
}

def parse_md():
    with open("markdown.md", "r") as m:
        lines = m.readlines()
    html = ""
    for line in lines:
        for pattern, tags in patterns.items():
            if pattern.match(line):
                html += f"\t{tags[0]}{line.strip()}{tags[1]}\n"
                break
    return html

html = """
<!DOCTYPE html>
<html>
"""
html += parse_md()
html += """
</html>
"""

# Write to an HTML file
with open("index.html", "w") as f:
    f.write(html)