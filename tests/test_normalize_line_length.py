import unittest
import json

from _normalize_line_length import normalize_line_length


class TestNormalizeLineLength(unittest.TestCase):
    SETTINGS_FILE_NAME = 'NormalizeLineLength.sublime-settings'
    TEST_FILE_NAME = 'test.txt'

    @classmethod
    def setUpClass(cls):
        with open(cls.SETTINGS_FILE_NAME) as settings_file:
            settings = json.load(settings_file)
        cls.ll = settings['max_line_length']
        with open ("tests/{}".format(cls.TEST_FILE_NAME)) as f:
            cls.test_string = f.read()

    def test_list(self):
        self.assertEqual(normalize_line_length(self.test_string), "hello")


if __name__ == '__main__':
    unittest.main()
