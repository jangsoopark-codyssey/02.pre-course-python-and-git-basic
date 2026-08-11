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

from game.quiz import Quiz
from game.quiz import QuizGame


class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.quiz = Quiz(
            category="국가와 수도",
            question="프랑스의 수도는 어디입니까?",
            choices=[
                "리옹",
                "마르세유",
                "파리",
                "니스"
            ],
            answer=3,
            hint="에펠탑이 있는 도시입니다."
        )

    def test_quiz_attributes(self):
        self.assertEqual(
            self.quiz.category,
            "국가와 수도"
        )

        self.assertEqual(
            self.quiz.question,
            "프랑스의 수도는 어디입니까?"
        )

        self.assertEqual(
            len(self.quiz.choices),
            4
        )

        self.assertEqual(
            self.quiz.answer,
            3
        )

        self.assertEqual(
            self.quiz.hint,
            "에펠탑이 있는 도시입니다."
        )

    def test_correct_answer(self):
        self.assertTrue(
            self.quiz.is_correct(3)
        )

    def test_wrong_answer(self):
        self.assertFalse(
            self.quiz.is_correct(1)
        )


class TestQuizGame(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.state_path = os.path.join(
            self.temp_dir.name,
            'state.json'
        )

        self.quizzes = [
            {
                "category": "국가와 수도",
                "question": "프랑스의 수도는 어디입니까?",
                "choices": [
                    "리옹",
                    "마르세유",
                    "파리",
                    "니스"
                ],
                "answer": 3,
                "hint": "에펠탑이 있는 도시입니다."
            }
        ]

        self.score = {
            "last": 0,
            "best": 0,
            "history": []
        }

        self.game = QuizGame(
            quizzes=self.quizzes,
            score=self.score,
            state_path=self.state_path
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_quiz_game_initialization(self):
        self.assertEqual(
            len(self.game.quizzes),
            1
        )

        self.assertEqual(
            self.game.quizzes[0].answer,
            3
        )

        self.assertEqual(
            self.game.score['best'],
            0
        )

    def test_score_update(self):
        self.game.score_update(
            score=4,
            num_questions=5
        )

        self.assertEqual(
            self.game.score['last'],
            4
        )

        self.assertEqual(
            self.game.score['best'],
            4
        )

        self.assertEqual(
            len(self.game.score['history']),
            1
        )

        history = self.game.score['history'][0]

        self.assertEqual(
            history['score'],
            4
        )

        self.assertEqual(
            history['num_questions'],
            5
        )

        self.assertIn(
            'datetime',
            history
        )

    def test_best_score_not_lowered(self):
        self.game.score['best'] = 5

        self.game.score_update(
            score=3,
            num_questions=5
        )

        self.assertEqual(
            self.game.score['best'],
            5
        )


if __name__ == '__main__':
    unittest.main()