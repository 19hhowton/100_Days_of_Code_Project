class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0 
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        """Returns the next question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(response, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True 
        return False
        
    def check_answer(self, response, answer):
        """Returns a print statement if the answer was correct"""
        if response.lower() == answer.lower():
            print("You answered correctly")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

