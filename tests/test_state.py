import json
import os
import sys
import tempfile
import unittest

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


class TestState(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.state_path = os.path.join(
            self.temp_dir.name,
            'state.json'
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_initialize(self):
        result = utils.initialize(
            self.state_path
        )

        self.assertTrue(result)

        self.assertTrue(
            os.path.exists(
                self.state_path
            )
        )

    def test_save_and_load_json(self):
        data = {
            "name": "quiz",
            "score": 10
        }

        result = utils.save_json_file(
            self.state_path,
            data
        )

        self.assertTrue(result)

        loaded = utils.load_json_file(
            self.state_path
        )

        self.assertEqual(
            loaded,
            data
        )

    def test_load_state_creates_missing_file(self):
        self.assertFalse(
            os.path.exists(
                self.state_path
            )
        )

        state = utils.load_state(
            self.state_path
        )

        self.assertIsNotNone(state)

        self.assertTrue(
            os.path.exists(
                self.state_path
            )
        )

    def test_load_state_recovers_corrupted_json(self):
        with open(
            self.state_path,
            'w',
            encoding='utf-8'
        ) as file:
            file.write(
                '{ invalid json'
            )

        state = utils.load_state(
            self.state_path
        )

        self.assertIsNotNone(state)

        self.assertIn(
            'application',
            state
        )

        self.assertIn(
            'score',
            state
        )

        self.assertIn(
            'quizzes',
            state
        )

    def test_update_state_preserves_existing_data(self):
        original = {
            "application": {
                "title": "Test Quiz"
            },
            "score": {
                "last": 0,
                "best": 0,
                "history": []
            },
            "quizzes": []
        }

        utils.save_json_file(
            self.state_path,
            original
        )

        new_score = {
            "last": 3,
            "best": 3,
            "history": []
        }

        result = utils.update_state(
            self.state_path,
            score=new_score
        )

        self.assertTrue(result)

        updated = utils.load_json_file(
            self.state_path
        )

        self.assertEqual(
            updated['score'],
            new_score
        )

        self.assertEqual(
            updated['application'],
            original['application']
        )

        self.assertEqual(
            updated['quizzes'],
            original['quizzes']
        )


if __name__ == '__main__':
    unittest.main()