import os
import sys
import unittest
from unittest.mock import patch

project_root = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

src_path = os.path.join(
    project_root,
    'src'
)

sys.path.insert(
    0,
    src_path
)

from common import utils


class TestInputText(unittest.TestCase):

    @patch(
        'builtins.input',
        side_effect=['hello']
    )
    def test_valid_input(self, mock_input):
        value = utils.input_text(
            '입력: '
        )

        self.assertEqual(
            value,
            'hello'
        )

    @patch(
        'builtins.input',
        side_effect=['', 'hello']
    )
    def test_empty_input_retry(self, mock_input):
        value = utils.input_text(
            '입력: '
        )

        self.assertEqual(
            value,
            'hello'
        )

        self.assertEqual(
            mock_input.call_count,
            2
        )

    @patch(
        'builtins.input',
        side_effect=['   hello   ']
    )
    def test_strip_input(self, mock_input):
        value = utils.input_text(
            '입력: '
        )

        self.assertEqual(
            value,
            'hello'
        )


class TestInputNumber(unittest.TestCase):

    @patch(
        'builtins.input',
        side_effect=['3']
    )
    def test_valid_number(self, mock_input):
        value = utils.input_number(
            '숫자: ',
            1,
            5
        )

        self.assertEqual(
            value,
            3
        )

    @patch(
        'builtins.input',
        side_effect=['abc', '3']
    )
    def test_invalid_string_retry(self, mock_input):
        value = utils.input_number(
            '숫자: ',
            1,
            5
        )

        self.assertEqual(
            value,
            3
        )

        self.assertEqual(
            mock_input.call_count,
            2
        )

    @patch(
        'builtins.input',
        side_effect=['0', '6', '4']
    )
    def test_out_of_range_retry(self, mock_input):
        value = utils.input_number(
            '숫자: ',
            1,
            5
        )

        self.assertEqual(
            value,
            4
        )

        self.assertEqual(
            mock_input.call_count,
            3
        )


class TestInputYesNo(unittest.TestCase):

    @patch(
        'builtins.input',
        side_effect=['y']
    )
    def test_yes(self, mock_input):
        value = utils.input_yes_no(
            '힌트? '
        )

        self.assertEqual(
            value,
            'y'
        )

    @patch(
        'builtins.input',
        side_effect=['N']
    )
    def test_case_insensitive(self, mock_input):
        value = utils.input_yes_no(
            '힌트? '
        )

        self.assertEqual(
            value,
            'n'
        )

    @patch(
        'builtins.input',
        side_effect=['abc', 'y']
    )
    def test_invalid_yes_no_retry(self, mock_input):
        value = utils.input_yes_no(
            '힌트? '
        )

        self.assertEqual(
            value,
            'y'
        )

        self.assertEqual(
            mock_input.call_count,
            2
        )


if __name__ == '__main__':
    unittest.main()