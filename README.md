# NormalizeLineLength
A cross-language [Sublime Text](http://www.sublimetext.com/) plugin for sorting items in a list. Handles lists without opening and closing list delimiters, and lists with trailing commas. Preserves lists' quote style (single vs. double).

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)


## Demo
![](https://github.com/kylebebak/sublime_normalize_line_length/blob/master/demo/normalize.gif)


## Installation

#### From Package Control
`NormalizeLineLength` is available via [Sublime Package Control](https://sublime.wbond.net/packages/NormalizeLineLength). This is the recommended way to install the plugin.

#### From GitHub
Alternatively, you may install via GitHub by cloning this repository into the `Packages`
directory under Sublime Text's data directory. For example, on OSX:

```
cd "~/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/kylebebak/sublime_normalize_line_length.git
```


## Usage
Highlight one or more lists and run the command. If the lists can't be sorted exceptions with line numbers will be displayed in the __quick panel__.

The name of the command is `normalize_line_length`. It appears in the `Command Palette` as `Sort List`. If you want to use it with a minimum of hassle add a shortcut to your `.sublime-keymap`.

```json
{ "keys": ["shift+alt+super+o"], "command": "normalize_line_length" }
```

If you want to change the list delimiter characters, override [NormalizeLineLength.sublime-settings](./NormalizeLineLength.sublime-settings).


## Tests
From the root directory, run `python3 -m unittest discover --verbose`. Some of the tests will fail in Python 2, but the plugin still works fine in Sublime Text 2.


## Contributing
Fork it and create a pull request.


## License
This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
