from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain        
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20)
        self.window.configure(background=THEME_COLOR)
        
        ## Question Background
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width=288,
            text="Question text here...", 
            font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        ## Score Text
        
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        self.get_next_question()
         
        ## Correct Button
        """Why was the button not working?? In order to use functions 
        in other files, from other CLASSES, you have to initialize that class along with this class. 
        After initialization, create an attribute to access the class attributes and methods.
        If you want a cookie, 
        you have to create that cookie, and then have a way to access the cookie
        ex. command = self.quiz.next_question ===>> quiz is from here!!!:
        def __init__(self, quiz_brain: QuizBrain):
            self.quiz = quiz_brain    
        """
        self.correct_img = PhotoImage(file=r"34_Trivia\images\true.png")
        self.correct_button = Button(image=self.correct_img, 
                                     highlightthickness=0, 
                                     command = self.correct_button)

        self.correct_button.grid(column=0, row=2)
        
        ## Incorrect Button
        self.incorrect_img = PhotoImage(file=r"34_Trivia\images\false.png")
        self.incorrect_button = Button(image=self.incorrect_img, 
                                       highlightthickness=0,
                                       command= self.incorrect_button)
        self.incorrect_button.grid(column=1, row=2)
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        
    def correct_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        
    def incorrect_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
       
        
    def give_feedback(self, is_right):
        """
        for ONLY 1000ms I want the canvas to be green
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        
        
