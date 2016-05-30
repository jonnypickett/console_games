from Games.MathQuiz.Questions.question import Question


class Subtract(Question):
    def __init__(self, num1, num2):
        if num1 >= num2:
            self.answer = num1 - num2
            self.text = '{} - {}'.format(num1, num2)
        else:
            self.answer = num2 - num1
            self.text = '{} - {}'.format(num2, num1)
