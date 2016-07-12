import unittest
import json

from normalize_line_length import normalize_line_length


class TestNormalizeLineLength(unittest.TestCase):
    SETTINGS_FILE_NAME = 'NormalizeLineLength.sublime-settings'

    @classmethod
    def setUpClass(cls):
        with open(cls.SETTINGS_FILE_NAME) as settings_file:
            settings = json.load(settings_file)
        cls.ll = settings['max_line_length']

    def test_list(self):
        self.assertEqual(self.sorted_string("['dog', 'cat', 'mouse']"),
                                            "['cat', 'dog', 'mouse']")

    def test_tuple(self):
        self.assertEqual(self.sorted_string("('dog', 'cat', 'mouse')"),
                                            "('cat', 'dog', 'mouse')")

    def test_trailing_comma(self):
        self.assertEqual(self.sorted_string("['dog', 'cat', 'mouse',]"),
                                            "['cat', 'dog', 'mouse',]")

    def test_no_delimiters(self):
        self.assertEqual(self.sorted_string("'dog', 'cat', 'mouse'"),
                                            "'cat', 'dog', 'mouse'")

    def test_whitespace(self):
        self.assertEqual(self.sorted_string("\n'dog',\n\n 'cat', 'mouse' \n"),
                                            "'cat', 'dog', 'mouse'")

    def test_whitespace_trailing_comma(self):
        self.assertEqual(self.sorted_string("('dog', 'cat', 'mouse'  , ) "),
                                            "('cat', 'dog', 'mouse',)")

    def test_double_quotes(self):
        self.assertEqual(self.sorted_string('("dog", "cat", "mouse")'),
                                            '("cat", "dog", "mouse")')

    def test_mixed_quotes(self):
        self.assertEqual(self.sorted_string("('dog', \"cat\", 'mouse')"),
                                            "('cat', 'dog', 'mouse')")

    def test_non_matching_delimiters(self):
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("['dog', 'cat', 'mouse'")
            self.assertEqual("List delimiters don't match", str(cm.exception))
        with self.assertRaises(SyntaxError) as cm:
            self.sorted_string("['dog', 'cat', 'mouse')")
            self.assertEqual("List delimiters don't match", str(cm.exception))

    def test_not_parsable(self):
        with self.assertRaises(ValueError) as cm:
            self.sorted_string("'dog', 'cat', 'mouse")
            self.assertEqual("List could not be parsed", str(cm.exception))

    def test_unorderable(self):
        with self.assertRaises(TypeError) as cm:
            self.sorted_string("['dog', 'cat', 1]")
            self.assertEqual("The list contains unorderable types", str(cm.exception))


if __name__ == '__main__':
    unittest.main()
