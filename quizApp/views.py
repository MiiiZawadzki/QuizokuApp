from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, Question_data_model
from django.views.decorators.csrf import csrf_exempt
from random import choice
import json
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    questions = Question.objects.all()
    question = choice(questions)
    
    question_data = Question_data_model(question.id, question.question, question.answers.split(';'), question.correct_answer)
    # question_data.id = question.id
    # question_data.question = question.question
    # question_data.answers = question.answers.split(';')
    # question_data.correct_answer = question.correct_answer
    # question = choice(questions)

    return render(request, 'index.html', {"question": question_data})

@csrf_exempt
def checkAnswer(request):
    if request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_id = body['questionId']    
        selected = body['selected']  
    
        question = Question.objects.get(id=int(question_id))

        return JsonResponse({"result":question.correct_answer == selected}) 
    return JsonResponse({"result":False}) 

@csrf_exempt
def loadNext(request):
    if request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_id = body['questionId'] 

        questions = Question.objects.all()
        question = choice(questions)
    
        question_data = Question_data_model(question.id, question.question, question.answers.split(';'), question.correct_answer)

        
        while(question.id == int(question_id)):
            question = choice(questions)
            question_data = Question_data_model(question.id, question.question, question.answers.split(';'), question.correct_answer)

        html = render_to_string('question.html', {"question": question_data})
        return HttpResponse(html)