import sys
sys.path.append(r"C:\Users\heath\Documents\My_Git_Hub\100_Days_of_Code_Project\17_Quizlet_Project")

from question_model import Question
from quiz_brain import QuizBrain
from open_trivia_data import question_data

def clean_text(text):
    """ Remove the &quot; from quTrueestion
    Text is a string. Returns a string without '&quot;'"""
    text_1 = text.replace('&quot;', '')
    cleaned_text = text_1.replace('&#039', '')
    print(cleaned_text)
    return cleaned_text



question_bank = []
for dict in question_data:
    text = dict["question"]
    cleaned_text = clean_text(text)
    answer = dict["correct_answer"]
    question_bank.append(Question(cleaned_text, answer))

# for q_obj in question_bank:
#     print(q_obj.text)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")