"""
initialize a question number, question list and user score.
"""
import html
class QuizBrain:
    def __init__(self,q_list):
        self.q_number = 0
        self.q_list = q_list
        self.user_score = 0
    """
    asks a question from the question list, stores the user's answer 
    and sends the user's answer to the checking function
    """
    def ask_question(self):
        converted_question = html.unescape((self.q_list[self.q_number].question)) # html unescaping
        return (converted_question)

    """
    compares the user's answer and the question's answer,
    if it is correct, add 1 point to the user's score and return "True" otherwise return 'False'.
    """
    def check_question(self,user_answer : str):
        is_answer_corrected = False
        if user_answer.lower() == self.q_list[self.q_number].answer.lower():
            self.user_score += 1
            is_answer_corrected = True
        self.q_number += 1
        return is_answer_corrected


    """
    compares the question quantities and questions in the list, if all questions are asked then return 'False'
    otherwise, return 'True'
    """
    def any_new_question(self):
        if self.q_number==len(self.q_list):
            return False
        else:
            return True