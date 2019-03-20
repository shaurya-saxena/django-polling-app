from django.shortcuts import render
from .models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.htm', context)

def detail(request, question_id):
    q = Question.objects.get(id=question_id)
    q_text = q.question_text
    context = {
        'q_text': q_text
    }
    return render(request, 'polls/detail.htm', context)

def results(request, question_id):
    q = Question.objects.get(id=question_id)
    q_text = q.question_text
    q_id = q.id
    context = {
        'q_text': q_text, 
        'q_id': q_id,
    }
    return render(request, 'polls/results.htm', context)


def vote(request, question_id):
    q = Question.objects.get(id=question_id)
    q_text = q.question_text
    q_id = q.id
    context = {
        'q_text': q_text, 
        'q_id': q_id,
    }
    return render(request, 'polls/vote.htm', context)
