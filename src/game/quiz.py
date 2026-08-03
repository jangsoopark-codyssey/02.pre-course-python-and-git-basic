

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

    # --------------------------------------------------------------------------------------------------------------------------s
    # Quiz Method
    # --------------------------------------------------------------------------------------------------------------------------s
    def quiz_solve(self, num_questions=5):
        print(f"퀴즈를 시작합니다! (총 {num_questions}문제)")
        score = 0
        for i in range(num_questions):
            quiz = self.quizzes[i]
            print(f"문제 {i + 1}: {quiz.question}")
            for j, choice in enumerate(quiz.choices):
                print(f"{j + 1}. {choice}")
            
            answer = int(input("\n정답을 입력하세요 (1-4): ").strip())
            if answer == quiz.answer:
                print("정답입니다!")
                score += 1
            else:
                print(f"오답입니다! 정답은 '{quiz.answer}'입니다.")

            print()  # Print a newline for better readability between questions
        print(
            f"퀴즈가 종료되었습니다.\n"
            f"당신의 점수는 {score}/{num_questions}입니다."
        )

        self.highest_score_update(score)

    def quiz_add(self):
        
        quiz = Quiz(question=question, answer="")
        
        print(f"새로운 퀴즈를 추가합니다.")
        quiz.question  = input("질문을 입력하세요: ")
        
        for i in range(4):
            choice = input(f"선택지 {i + 1}를 입력하세요: ")
            quiz.choices.append(choice)
        quiz.answer = input("정답을 입력하세요: ")        

        self.quizzes.append(quiz)

        print("퀴즈가 추가되었습니다.")

    def quiz_list(self):
        print(f"등록된 퀴즈 목록: 총 {len(self.quizzes)}문제")
        for i, quiz in enumerate(self.quizzes):
            print(f"{i + 1}. {quiz.question}")

    def highest_score_update(self, score):
        if score > self.highest_score:
            self.highest_score = score
            print(f"최고 점수가 갱신되었습니다! 새로운 최고 점수: {self.highest_score}")

    def highest_score_show(self):
        print(f"현재 최고 점수: {self.highest_score}")
