# application.py

from common import utils
from game import quiz


class Application(object):

    def __init__(self, name, **params):
        self._name = name
        self._menu = params.get('menu')
        self._divider_width = params.get('divider_width', 50)
        self._quizzes = params.get('quizzes', [])
        self._score = params.get(
            'score',
            {
                'last': 0,
                'best': 0,
                'history': []
            }
        )
        self._state_path = params.get('state_path')

        self._quiz_game = quiz.QuizGame(
            self._quizzes,
            self._score,
            self._state_path
        )

    def menu(self):
        print('=' * self._divider_width)
        print(f"\t\t{self._name}!")
        print('=' * self._divider_width)

        for i, option in enumerate(
            self._menu['options'],
            start=1
        ):
            print(f"{i}. {option}")

        print('=' * self._divider_width)

        return utils.input_number(
            self._menu['prompt'],
            1,
            len(self._menu['options'])
        )

    def run(self):
        running = True

        while running:
            choice = self.menu()
            print()

            match choice:
                case 1:
                    self._quiz_game.quiz_solve()

                case 2:
                    self._quiz_game.quiz_add()

                case 3:
                    self._quiz_game.quiz_list()

                case 4:
                    self._quiz_game.quiz_delete()

                case 5:
                    self._quiz_game.score_show()

                case 6:
                    self._quiz_game.score_history_show()

                case 7:
                    running = False

                case _:
                    print(
                        f"\n1~{len(self._menu['options'])} 사이의 숫자를 "
                        "다시 입력해주세요.\n"
                    )
