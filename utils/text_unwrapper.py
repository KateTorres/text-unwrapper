# Un-wrapping module :
### Removes leading and training whitespace.
### If line is empty - makes a paragraph.

import re

def unwrap_text(text):
    lines = text.splitlines()
    paragraphs = []
    buffer = []

    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            if buffer:
                paragraphs.append(" ".join(buffer))
                buffer = []
            continue

        buffer.append(line)

        # Look ahead for new paragraph if next line is capitalized and current ends in punctuation
        if (
            i + 1 < len(lines) and
            lines[i + 1].strip() and
            re.match(r"^[А-ЯA-Z]", lines[i + 1].strip()) and
            re.search(r"[.!?]$", line)
        ):
            paragraphs.append(" ".join(buffer))
            buffer = []

    if buffer:
        paragraphs.append(" ".join(buffer))

    return "\n\n".join(paragraphs)
