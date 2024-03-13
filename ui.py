from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface():
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        # define UI window
        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx = 30, pady = 30, bg = THEME_COLOR)
        
        # define a score label on the right top of the window, and keep the score of the user.
        self.score_label = Label(text = f"Score: 0", bg = "white", fg = THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        # define a canvas for questions, in the middle of the window
        self.text_canvas = Canvas(width=300, height=280, bg = "white", highlightbackground = THEME_COLOR)
        self.question_text = self.text_canvas.create_text(
            150,
            140,
            width = 270,
            text = "Questions", 
            fill = THEME_COLOR,
            font= ("Arial", 20, "italic")
            )
        self.text_canvas.grid(row = 1, column = 0, columnspan = 2, pady=10)
        
        
        # define a false button on the left bottom of the window, and it calls 'false_button_pressed' function.
        false_image = PhotoImage(file = "images/false.png")
        self.false_button = Button(image = false_image, highlightbackground = THEME_COLOR, command = self.false_button_pressed)
        self.false_button.grid(row=2, column=0)
        
        # define a true button on the right bottom of the window, and it calls 'true_button_pressed' function.
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image = true_image, highlightbackground = THEME_COLOR, command = self.true_button_pressed)
        self.true_button.grid(row=2, column=1)
        
        # call a function that gets a new question from the 'QuizBrain' class.
        self.get_new_question() 
       
        # keep the window on
        self.window.mainloop()
        
    def get_new_question(self):
        """
        sets the question canvas background color 'white'
        keeps asking questions if any new questions available otherwise sends a text instead of a new question,
        and disable both buttons on the window.
        """
        self.text_canvas.config(bg = "white")   
        if self.quiz.any_new_question():
            """
            updates the user score, gets a new question from the quiz object, 
            and sends the question to the window.
            """
            self.score_label.config(text=f"Score: {self.quiz.user_score} / {self.quiz.q_number + 1}") 
            new_question = self.quiz.ask_question() 
            self.text_canvas.itemconfig(self.question_text, text = new_question)
        else:
            """
            changes the question text properties
            sends a message that all questions have been asked.
            disables the buttons on the window.
            """
            self.text_canvas.itemconfig(self.question_text, font= ("Arial", 30, "bold"))
            self.text_canvas.itemconfig(self.question_text, text = "Congrats!, You have completed the quiz.") # 
            self.true_button.config(state = "disabled") # disable the true button.
            self.false_button.config(state = "disabled") # disable the true button.
           
            
        
    def true_button_pressed(self):
        """
        asks the answer of the question,
        if it is 'true', sets the question background-color 'green' for 1 sec then calls 'get_new_question' func.
        if not, sets the question background-color 'red' for 1 sec then calls 'get_new_question' func.      
        """
        if self.quiz.check_question("true"):
            self.text_canvas.config(bg = "green")
            self.window.after(1000,self.get_new_question)
        else:
            self.text_canvas.config(bg = "red")
            self.window.after(1000,self.get_new_question)

            
    def false_button_pressed(self):
        """
        asks the answer of the question,
        if it is 'false', sets the question background-color 'green' for 1 sec then calls 'get_new_question' func.
        if not, sets the question background-color 'red' for 1 sec then calls 'get_new_question' func.      
        """
        if self.quiz.check_question("false"):
            self.text_canvas.config(bg = "green")
            self.window.after(1000,self.get_new_question)
        else:
            self.text_canvas.config(bg = "red")
            self.window.after(1000,self.get_new_question)
 
        