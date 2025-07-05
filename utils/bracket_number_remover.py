# utils/bracket_number_remover.py
import re

# strip any whitespace (incl. new-lines) around a digits-only bracket token
_BRACKET_NUM_RE = re.compile(r'\s*\[\d+\]\s*', re.MULTILINE)

# replace SINGLE line breaks (not part of a double) with one space
_SINGLE_NL_RE = re.compile(r'(?<!\n)\n(?!\n)')

def remove_bracket_numbers(text: str) -> str:
    """
    Delete bracketed numeric references like “[23]” and pull the surrounding
    text together. A true blank line (≥2 consecutive new-lines) is treated as a
    paragraph boundary and is left intact.
    """
    # 1) remove the numeric bracket tokens
    without_refs = _BRACKET_NUM_RE.sub(" ", text)

    # 2) collapse single line breaks to spaces
    merged = _SINGLE_NL_RE.sub(" ", without_refs)

    # 3) normalise runs of spaces/tabs
    merged = re.sub(r'[ \t]{2,}', ' ', merged)

    return merged.strip()
