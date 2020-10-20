from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Question # also need to import Choice
from .models import Weather
# we will need a reverse URL lookup
from django.urls import reverse

# it's a good idea to pass sensible defaults to views
def index(request): # by convention the home page is called index
    # iterate over every member in our question collection
    latest_question_list = Question.objects.order_by('-pub_date')[:3]
    # output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    # better way - use the 'render' shortcut
    context = {'latest_question_list': latest_question_list}
    #     original request, template, context
    return render(request, 'polls/index.html', context)

# we an use our 404 shortcut here
def detail(request, question_id=1): # we can pass a parameter as 'question_id'
    # recommend using get_object_or_404
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})
    # return HttpResponse("Here's detals of question {}".format(question_id) ) # we can pass parameters

def results(request, question_id=1):
    # return HttpResponse('Results for question {}'.format(question_id) )
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def demo_form(request):
    return render(request, 'polls/demo_form.html' )

def weather(request):
    weather_list = Weather.objects.order_by('city') 
    context = {'weather_list': weather_list}
    return render(request, 'polls/weather.html', context)

def weather_form(request, weather_id):
    # is it GET or POST?
    if request.method =='POST':
        # the form has been submitted, so save the changes and then show the 'weather' view
        selected_weather = get_object_or_404(Weather, pk=request.POST['id'])
        selected_weather.country = request.POST['country']
        selected_weather.city = request.POST['city']
        selected_weather.description = request.POST['description']
        selected_weather.temperature = request.POST['temperature']
        selected_weather.save()
        weather_list = Weather.objects.order_by('city') 
        context = {'weather_list': weather_list}
        return render(request, 'polls/weather.html', context)
    else:
        # for form has NOT yet been submitted - just show the weather_form view
        weather = get_object_or_404(Weather, pk=weather_id)
        context = {'weather':weather}
        return render(request, 'polls/weather_form.html', context)

