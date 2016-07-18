# NormalizeLineLength
A [Sublime Text](http://www.sublimetext.com/) plugin for grabbing multiple lines of text and normalizing the line length. Splits lines only on spaces. Preserves leading spaces. Particularly handy for comments and docstrings.

- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [Contributing](#contributing)
- [License](#license)


## Demo
![](https://github.com/kylebebak/sublime_normalize_line_length/blob/master/demo/normalize.gif)


## Installation

#### Package Control

#### From GitHub
Alternatively, you may install via GitHub by cloning this repository into the `Packages`
directory under Sublime Text's data directory. For example, on OSX:

```
cd "~/Library/Application Support/Sublime Text 3/Packages"
git clone https://github.com/kylebebak/sublime_normalize_line_length.git
```


## Usage
Highlight text. Run command. If the text contains a word whose length exceeds the max line length, an exception will be displayed in the __quick panel__.

The name of the command is `normalize_line_length`. It appears in the `Command Palette` as `Normalize`. If you want to use it with a minimum of hassle add a shortcut to your `.sublime-keymap`.

```json
{ "keys": ["ctrl+alt+super+n"], "command": "normalize_line_length" }
```

The default max line length is __80 chars__. If you want to change this, override `max_line_length` in [NormalizeLineLength.sublime-settings](./NormalizeLineLength.sublime-settings).

### Windows Line Endings

If your file has Windows line endings (__carriage return__ + __line feed__), set your line endings to `Unix` under __View -> Line Endings__ before running the plugin. `NormalizeLineLength` doesn't quite work as advertised for Windows line endings.


## Tests
From the root directory, run `python3 -m unittest discover --verbose`.


## Contributing
Fork it and create a pull request.


## License
This code is licensed under the [MIT License](https://opensource.org/licenses/MIT).
