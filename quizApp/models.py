from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    answers = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=300)

class Question_data_model():
    def __init__(self, id, question, answers, correct_answer):
        self.id = id
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer

questions = [
    Question_data_model(id=1, question="How many teeth does an adult rabbit have?", answers=["28","30","26","24"], correct_answer="28"),
    Question_data_model(id=2, question="How many legs do butterflies have?", answers=["2","4","6","0"], correct_answer="6"),
    Question_data_model(id=3, question="What colour is the female blackbird?", answers=["Black","Brown","White","Yellow"], correct_answer="Brown"),
    Question_data_model(id=4, question="What do you call a baby bat?", answers=["Cub","Chick","Kid","Pup"], correct_answer="Pup"),
    Question_data_model(id=5, question="Hippocampus is the Latin name for which marine creature?", answers=["Dolphin","Whale","Octopus","Seahorse"], correct_answer="Seahorse"),
    Question_data_model(id=6, question="By definition, where does an abyssopelagic animal live?", answers=["In the desert","At the bottom of the ocean","On top of a mountain","Inside a tree"], correct_answer="At the bottom of the ocean"),
    Question_data_model(id=7, question="What is the collective noun for a group of crows?", answers=["Pack","Gaggle","Murder","Herd"], correct_answer="Murder")
]