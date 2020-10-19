from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Question

# it's a good idea to pass sensible defaults to views
def index(request): # by convention the home page is called index
    # iterate over every member in our question collection
    latest_question_list = Question.objects.order_by('-pub_date')
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # better way - use the 'render' shortcut
    context = {'latest_question_list': latest_question_list}
    #     original request, template, context
    return render(request, 'polls/index.html', context)


def detail(request, question_id=1): # we can pass a parameter as 'question_id'
    return HttpResponse("Here's detals of question {}".format(question_id) ) # we can pass parameters

def results(request, question_id=1):
    return HttpResponse('Results for question {}'.format(question_id) )

def vote(request, question_id=1):
    return HttpResponse('Here you can vote on question {}'.format(question_id) )






def weather(request):
    return HttpResponse('This is the Weather page')
