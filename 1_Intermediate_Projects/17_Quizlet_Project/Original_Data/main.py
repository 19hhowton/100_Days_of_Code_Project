import sys
sys.path.append(r"C:\Users\heath\Documents\My_Git_Hub\100_Days_of_Code_Project\17_Quizlet_Project")

from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for dict in question_data:
    text = dict["text"]
    answer = dict["answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")