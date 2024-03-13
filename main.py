from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

parameters ={
    "amount": 10,
    "type": "boolean"
    
}

response = requests.get("https://opentdb.com/api.php", params = parameters)
response.raise_for_status
data = response.json()

question_bank = [] # a list used to store questions and their answer.
game_on = True # a variable enables game loop

def create_question_bank():
    """
    reading question data from data, storing questions and their answers and adding to a list variable.
    """
    for index in  range(len(data["results"])):
        new_question = Question(question = data["results"][index]["question"], answer = data["results"][index]["correct_answer"])
        question_bank.append(new_question)

create_question_bank() # calls the function to assign questions and answers to the 'question_bank' list
main_quiz_brain = QuizBrain(question_bank) # creates an object to use in a game loop.
main_ui = QuizInterface(main_quiz_brain)
