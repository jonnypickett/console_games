from Games.MathQuiz.Questions.question import Question


class Divide(Question):
    def __init__(self, num1, num2):
        self.answer = num1 / num2
        self.text = '{} / {}'.format(num1, num2)