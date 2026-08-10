from common import definitions


class Quiz(object):
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer


class QuizGame(object):
    def __init__(self, quizzes):
        self.quizzes = [
            Quiz(question=quiz['question'], choices=quiz['choices'], answer=quiz['answer']) 
            for quiz in quizzes
        ]
        self.highest_score = 0

    # --------------------------------------------------------------------------------------------------------------------------
    # Quiz Method
    # --------------------------------------------------------------------------------------------------------------------------
    def quiz_solve(self, num_questions=5):
        # TODO: Refactoring - with New Branch 
        if not len(self.quizzes):
            print("등록된 퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return

        num_questions = min(num_questions, len(self.quizzes))

        print(f"퀴즈를 시작합니다! (총 {num_questions}문제)")
        score = 0
        
        i = 0
        while i < num_questions:
            
            quiz = self.quizzes[i]
            print(f"문제 {i + 1}: {quiz.question}")
            for j, choice in enumerate(quiz.choices):
                print(f"{j + 1}. {choice}")
            
            try:
                answer = int(input("\n정답을 입력하세요 (1-4): ").strip())
                if answer < 1 or answer > 4:
                    raise ValueError("정답은 1~4 사이의 숫자여야 합니다.")
            except ValueError:
                print("잘못된 입력입니다. 1~4 사이의 숫자를 입력해주세요.")
                continue
            except KeyboardInterrupt:
                # Ignore the interrupt and proceed to the current question
                print("\nCtrl+C 입력은 사용할 수 없습니다. 다시 입력해주세요.")
                continue
            except EOFError:
                # Ignore the EOF and proceed to the current question
                print("\n입력이 종료되었습니다. 다시 입력해주세요.")
                continue

            # Print Result
            if answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다! 정답은 '{quiz.answer}'입니다.")
            print()  # Print a newline for better readability between questions

            # Increment the question index only if the answer was valid (1-4)
            i += 1
            
        print(
            f"퀴즈가 종료되었습니다.\n"
            f"당신의 점수는 {score}/{num_questions}입니다."
        )

        self.highest_score_update(score)

    def quiz_add(self):
        print("새로운 퀴즈를 추가합니다.")

        quiz = Quiz(question="", choices=[], answer="")

        # Question
        while True:
            try:
                quiz.question = input("질문을 입력하세요: ").strip()

                if not quiz.question:
                    print("질문을 입력해주세요.")
                    continue

                break

            except KeyboardInterrupt:
                # Ignore the interrupt and proceed
                print("\nCtrl+C 입력은 사용할 수 없습니다.")
                continue

            except EOFError:
                # Ignore the EOF and proceed
                print("\n입력이 종료되었습니다. 다시 입력해주세요.")
                continue

        # Choices
        i = 0
        while i < definitions.max_num_choices:
            try:
                choice = input(f"선택지 {i + 1}를 입력하세요: ").strip()

                if not choice:
                    print("선택지를 입력해주세요.")
                    continue

            except KeyboardInterrupt:
                # Ignore the interrupt and proceed
                print("\nCtrl+C 입력은 사용할 수 없습니다.")
                continue

            except EOFError:
                # Ignore the EOF and proceed
                print("\n입력이 종료되었습니다. 다시 입력해주세요.")
                continue

            quiz.choices.append(choice)
            i += 1

        # TODO: Refactoring - with New Branch
        while True:
            try:
                quiz.answer = int(
                    input(
                        f"정답을 입력하세요 (1-{definitions.max_num_choices}): "
                    ).strip()
                )

                if quiz.answer < 1 or quiz.answer > definitions.max_num_choices:
                    print(
                        f"잘못된 입력입니다. "
                        f"1~{definitions.max_num_choices} 사이의 숫자를 입력해주세요."
                    )
                    continue

                break

            except ValueError:
                print(
                    f"잘못된 입력입니다. "
                    f"1~{definitions.max_num_choices} 사이의 숫자를 입력해주세요."
                )

            except KeyboardInterrupt:
                # Ignore the interrupt and proceed
                print("\nCtrl+C 입력은 사용할 수 없습니다.")
                continue

            except EOFError:
                # Ignore the EOF and proceed
                print("\n입력이 종료되었습니다. 다시 입력해주세요.")
                continue

        self.quizzes.append(quiz)

        print("퀴즈가 추가되었습니다.")

    def quiz_list(self):
        # TODO: Refactoring - with New Branch 
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"등록된 퀴즈 목록: 총 {len(self.quizzes)}문제")
        for i, quiz in enumerate(self.quizzes):
            print(f"{i + 1}. {quiz.question}")

    # --------------------------------------------------------------------------------------------------------------------------
    # Score Method
    # --------------------------------------------------------------------------------------------------------------------------
    def highest_score_update(self, score):
        if score > self.highest_score:
            self.highest_score = score
            print(f"최고 점수가 갱신되었습니다! 새로운 최고 점수: {self.highest_score}")

    def highest_score_show(self):
        print(f"현재 최고 점수: {self.highest_score}")
