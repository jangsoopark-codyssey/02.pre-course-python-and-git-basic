from game import quiz


class Application(object):
    def __init__(self, name, **params):
        self._name = name
        self._menu = params.get('menu')
        self._divider_width = params.get('divider_width', 50)
        self._quizzes = params.get('quizzes', [])

        self.quiz_game = quiz.QuizGame(self._quizzes)

    def menu(self):
        # Title 
        print('=' * self._divider_width)
        print(f"\t\t{self._name}!")
        print('=' * self._divider_width)

        # Menu Options
        for i, option in enumerate(self._menu['options'], start=1):
            print(f"{i}. {option}")

        print('=' * self._divider_width)
        
        # Prompt for user input with error handling for invalid input
        try:
            return int(input(f'{self._menu["prompt"]}').strip())
        except ValueError:
            return -1
        except KeyboardInterrupt:
            # Ignore the interrupt and proceed to the current question
            continue
        except EOFError:
            # Ignore the EOF and proceed to the current question
            continue

    def run(self):
        _running = True

        while _running: 
            choice = self.menu()
            print()

            match choice:
                case 1:
                    self.quiz_game.quiz_solve()
                case 2:
                    self.quiz_game.quiz_add()
                case 3:
                    self.quiz_game.quiz_list()
                case 4:
                    self.quiz_game.highest_score_show()
                case 5:
                    _running = False
                case _:
                    print("\n\n 잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요. \n\n")
                    