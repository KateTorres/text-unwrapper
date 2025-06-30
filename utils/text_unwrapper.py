# Un-wrapping module :
### Removes leading and training whitespace.
### If line is empty - makes a paragraph.

def unwrap_text(text):
    lines = text.splitlines()
    paragraphs = []
    buffer = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if buffer:
                paragraphs.append(" ".join(buffer))
                buffer = []
        else:
            buffer.append(stripped)

    if buffer:
        paragraphs.append(" ".join(buffer))

    return "\n\n".join(paragraphs)
