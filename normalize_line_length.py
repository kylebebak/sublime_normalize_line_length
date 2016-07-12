def text_normalize_line_length(s, l=80):
    l = max(20, l)
    lines = s.split("\n")

    leading_spaces = 0
    for line in lines:
        ls = len(line) - len(line.lstrip(' '))
        if ls:
            leading_spaces = ls
            break
    l -= leading_spaces

    paragraphs = [' '.join(paragraph.split()) for paragraph in s.split("\n\n")]
    paragraphs = [p for p in paragraphs if p]
    for i, paragraph in enumerate(paragraphs):
        lines = []
        while len(paragraph) > l:
            line, paragraph = get_next_line_from_paragraph(paragraph, l)
            lines.append(line)
        lines.append(paragraph)
        paragraphs[i] = '\n'.join(["{}{}".format(' '*leading_spaces, line) for line in lines])
    return '\n\n'.join(paragraphs)


def get_next_line_from_paragraph(paragraph, l):
    if paragraph[l] is ' ':
        index = l
    else:
        last_space = paragraph[:l][::-1].find(' ')
        if last_space is -1:
            raise Exception("Word length exceeded line length")
        index = l-last_space
    return paragraph[:index-1], paragraph[index:]
