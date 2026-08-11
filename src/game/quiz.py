from common import definitions
from common import utils

import random


class Quiz(object):

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self, number=None):
        if number is not None:
            print(f"문제 {number}: {self.question}")
        else:
            print(self.question)

        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

    def is_correct(self, answer):
        return answer == self.answer


class QuizGame(object):

    def __init__(self, quizzes, highest_score, state_path=None):
        self.quizzes = [
            Quiz(
                question=quiz['question'],
                choices=quiz['choices'],
                answer=quiz['answer']
            )
            for quiz in quizzes
        ]

        self.highest_score = highest_score
        self.state_path = state_path

    # ----------------------------------------------------------------------------------------------------------------------
    # Quiz Method
    # ----------------------------------------------------------------------------------------------------------------------

    def quiz_solve(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return

        num_questions = utils.input_number(
            f"풀 문제 수를 입력하세요 "
            f"(1-{len(self.quizzes)}): ",
            1,
            len(self.quizzes)
        )

        selected_quizzes = random.sample(
            self.quizzes,
            num_questions
        )

        print(
            f"퀴즈를 시작합니다! "
            f"(총 {num_questions}문제)"
        )

        score = 0

        for i, quiz in enumerate(
            selected_quizzes,
            start=1
        ):
            quiz.show(i)

            answer = utils.input_number(
                f"\n정답을 입력하세요 "
                f"(1-{len(quiz.choices)}): ",
                1,
                len(quiz.choices)
            )

            if quiz.is_correct(answer):
                print("정답입니다!")
                score += 1
            else:
                print(
                    f"오답입니다! "
                    f"정답은 '{quiz.answer}'입니다."
                )

            print()

        print(
            f"퀴즈가 종료되었습니다.\n"
            f"당신의 점수는 "
            f"{score}/{num_questions}입니다."
        )

        self.highest_score_update(score)

    def quiz_add(self):
        print("새로운 퀴즈를 추가합니다.")

        question = utils.input_text(
            "질문을 입력하세요: "
        )

        choices = [
            utils.input_text(
                f"선택지 {i}를 입력하세요: "
            )
            for i in range(
                1,
                definitions.max_num_choices + 1
            )
        ]

        answer = utils.input_number(
            f"정답을 입력하세요 "
            f"(1-{definitions.max_num_choices}): ",
            1,
            definitions.max_num_choices
        )

        quiz = Quiz(
            question=question,
            choices=choices,
            answer=answer
        )

        self.quizzes.append(quiz)

        self.save()

        print("퀴즈가 추가되었습니다.")

    def quiz_list(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(
            f"등록된 퀴즈 목록: "
            f"총 {len(self.quizzes)}문제"
        )

        for i, quiz in enumerate(
            self.quizzes,
            start=1
        ):
            print(
                f"{i}. {quiz.question}"
            )

    # ----------------------------------------------------------------------------------------------------------------------
    # Score Method
    # ----------------------------------------------------------------------------------------------------------------------

    def highest_score_update(self, score):
        if score <= self.highest_score:
            return

        self.highest_score = score

        self.save()

        print(
            f"최고 점수가 갱신되었습니다! "
            f"새로운 최고 점수: "
            f"{self.highest_score}"
        )

    def highest_score_show(self):
        print(
            f"현재 최고 점수: "
            f"{self.highest_score}"
        )

    # ----------------------------------------------------------------------------------------------------------------------
    # State Method
    # ----------------------------------------------------------------------------------------------------------------------

    def save(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.highest_score
        }

        utils.save_json_file(
            self.state_path,
            data
        )