import re


def normalize_line_length(s, ll=80):
    """The workhorse for the plugin. More than two line breaks between
    non-whitespace text is treated as a paragraph. Paragraphs are normalized
    separately.
    """
    ll = max(20, ll)
    lines = s.split("\n")

    leading_spaces = 0
    for line in lines:
        ls = len(line) - len(line.lstrip(' '))
        if ls:
            leading_spaces = ls
            break
    ll -= leading_spaces

    paragraphs = [' '.join(paragraph.split()) for paragraph in re.split("\n *\n", s)]
    paragraphs = [p for p in paragraphs if p]
    for i, paragraph in enumerate(paragraphs):
        lines = []
        while len(paragraph) > ll:
            line, paragraph = get_next_line_from_paragraph(paragraph, ll)
            lines.append(line)
        lines.append(paragraph)
        paragraphs[i] = '\n'.join(["{}{}".format(' '*leading_spaces, line) for line in lines])
    return '\n\n'.join(paragraphs)


def get_next_line_from_paragraph(paragraph, ll):
    """Return the largest substring from `paragraph` that ends in a space and
    doesn't exceed `ll`. Raise exception f no such string exists.
    """
    if paragraph[ll] is ' ':
        index = ll+1
    else:
        last_space = paragraph[:ll][::-1].find(' ')
        if last_space is -1:
            raise Exception("Word length exceeded line length")
        index = ll-last_space
    return paragraph[:index-1], paragraph[index:]
