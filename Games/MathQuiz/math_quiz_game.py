import datetime
import random

from Games.MathQuiz.Questions.add import Add
from Games.MathQuiz.Questions.multiply import Multiply
from Games.MathQuiz.Questions.subtract import Subtract
from Games.game import Game
import utilities


class MathQuizGame(Game):
    """Manage Math Quiz Game game play"""
    ID = 5
    TITLE = "Math Quiz Game"
    DIFFICULTIES = {
        'e': {'total_questions': 10, 'max_number': 12, 'min_number': 1},
        'm': {'total_questions': 20, 'max_number': 20, 'min_number': 1},
        'h': {'total_questions': 30, 'max_number': 50, 'min_number': 1},
    }
    game_difficulty = None
    answers = []
    questions = []
    start_time = None
    end_time = None
    max_number = None
    min_number = None

    def ask(self, question):
        """Ask the question. Log the start time and end time.
        Return whether the player got the answer correct and
        the elapsed time.
        """
        correct = False
        question_start = datetime.datetime.now()
        answer = input(question.text + ' = ')
        if answer == str(question.answer):
            correct = True
        question_end = datetime.datetime.now()
        return correct, question_end - question_start

    def cleanup(self):
        """Clear the questions and answers lists"""
        self.answers = []
        self.questions = []

    def setup(self):
        """Generate 10 random questions and add them to questions."""
        self.set_difficulty()
        self.max_number = self.DIFFICULTIES[self.game_difficulty]['max_number']
        self.min_number = self.DIFFICULTIES[self.game_difficulty]['min_number']
        question_types = (Add, Multiply, Subtract)
        for _ in range(self.DIFFICULTIES[self.game_difficulty]['total_questions']):
            num1 = random.randint(self.min_number, self.max_number)
            num2 = random.randint(self.min_number, self.max_number)
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def start(self):
        """Begin the game."""
        super().start()
        utilities.clear_screen()
        self.show_welcome()
        self.setup()
        print("How many questions can you get right out of {}?".format(len(self.questions)))
        print("The clock is ticking, so you better hurry!")
        while self.playing and len(self.answers) < len(self.questions):
            self.start_time = datetime.datetime.now()
            for question in self.questions:
                self.answers.append(self.ask(question))
            else:
                self.playing = False
                self.end_time = datetime.datetime.now()

        else:
            self.show_summary()
            self.cleanup()

        self.play_again_prompt()

    def show_summary(self):
        """Print how many questions the player got right
        out of how many questions answered.
        Print how long it took the player to complete the quiz.
        """
        print("You got {} out of {} correct".format(
            self.total_correct(), len(self.questions)
        ))
        print("It took you {} seconds total.".format(
            (self.end_time-self.start_time).seconds
        ))

    def total_correct(self):
        """Return total number of questions answered correctly"""
        total = 0
        for answer in self.answers:
            if answer[0]:
                total += 1
        return total