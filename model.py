from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class CBT:
    def __init__(self):
        self.questions = []
        self.history_stack = []  # Stack (LIFO)

    def add_question(self, question):
        self.questions.append(question)

    def grade(self, answers):
        score = 0
        for i in range(len(self.questions)):
            if self.questions[i].check_answer(answers[i]):
                score += 1

        result = {
            "score": score,
            "total": len(self.questions),
            "time": datetime.now()
        }

        self.history_stack.append(result)  # push to stack
        return result

    def get_last_result(self):
        if self.history_stack:
            return self.history_stack[-1]
        return None