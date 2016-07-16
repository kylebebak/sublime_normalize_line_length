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

    def test_file(self):
        with open ("tests/test_check.txt") as f:
            test_string_check = f.read()
        test_string_normalized = normalize_line_length(self.test_string)
        l = min(len(test_string_check), len(test_string_normalized))
        self.assertEqual(normalize_line_length(test_string_normalized[:l]), test_string_check[:l])

    def test_max_length_and_last_char(self):
        import random
        for MAX_LENGTH in set(random.randint(40, 60) for i in range(10)):
            with open ("tests/dickens.txt") as f:
                string = normalize_line_length(f.read(), MAX_LENGTH)

            max_length = max(len(line) for line in string.split('\n'))
            self.assertEqual(MAX_LENGTH, max_length)

            for line in string.split('\n'):
                if line:
                    self.assertNotEqual(' ', line[-1])


if __name__ == '__main__':
    unittest.main()
