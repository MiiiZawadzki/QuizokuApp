from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Question, Question_data_model, questions
from django.views.decorators.csrf import csrf_exempt
from random import choice
import json
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    question = choice(questions)

    return render(request, 'index.html', {"question": question})

@csrf_exempt
def checkAnswer(request):
    if request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_id = body['questionId']    
        selected = body['selected']  
    
        question =  [quest for quest in questions if quest.id==int(question_id)][0]

        return JsonResponse({"result":question.correct_answer == selected}) 
    return JsonResponse({"result":False}) 

@csrf_exempt
def loadNext(request):
    if request.is_ajax():
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        question_id = body['questionId'] 

        question = choice(questions)
        
        while(question.id == int(question_id)):
            question = choice(questions)

        html = render_to_string('question.html', {"question": question})
        return HttpResponse(html)