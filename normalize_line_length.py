"""
NormalizeLineLength - Sublime Text Plugin

Best used for tidying up doc strings.

Prints exceptions to quick panel.
"""

import sublime, sublime_plugin

settings_filename = "NormalizeLineLength.sublime-settings"


class NormalizeLineLengthCommand(sublime_plugin.TextCommand):
    MAX_LINE_LENGTH = 80

    def run(self, edit):
        settings = sublime.load_settings(settings_filename)
        ll = settings.get("max_line_length") or self.START_LIST_CHARS

        view = self.view
        sel = view.sel()
        exceptions = []
        for region in sel: # handle multiple selection regions
            if not region.empty():
                try:
                    s = normalize_line_length(view.substr(region), ll)
                except Exception as e: # include line number with exception
                    exceptions.append("{}: {}".format(
                        view.rowcol(region.begin())[0] + 1, str(e)
                    ))
                else:
                    view.replace(edit, region, s)
        if exceptions:
            self.show_quick_panel(exceptions, self.view.window())

    def show_quick_panel(self, messages, window):
        window.show_quick_panel(messages, None, sublime.MONOSPACE_FONT)


def normalize_line_length(s, ll=80):
    ll = max(20, ll)
    lines = s.split("\n")

    leading_spaces = 0
    for line in lines:
        ls = len(line) - len(line.lstrip(' '))
        if ls:
            leading_spaces = ls
            break
    ll -= leading_spaces

    paragraphs = [' '.join(paragraph.split()) for paragraph in s.split("\n\n")]
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
    if paragraph[ll] is ' ':
        index = ll
    else:
        last_space = paragraph[:ll][::-1].find(' ')
        if last_space is -1:
            raise Exception("Word length exceeded line length")
        index = ll-last_space
    return paragraph[:index-1], paragraph[index:]
