"""
NormalizeLineLength - Sublime Text Plugin

Best used for tidying up doc strings.

Prints exceptions to quick panel.
"""

import sublime, sublime_plugin

from ._normalize_line_length import normalize_line_length

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
