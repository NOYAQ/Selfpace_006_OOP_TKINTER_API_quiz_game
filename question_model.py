"""
initialize a question and an answer attribute for a Question object.
"""
class Question:
    def __init__(self,question,answer) -> None:
        self.question = question
        self.answer = answer