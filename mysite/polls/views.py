from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from .models import Question # also need to import Choice
from .models import Weather
# we will need a reverse URL lookup
from django.urls import reverse
from django.views import generic

# we replace the function index, result and detail with Class-based views
# Class based views descend from generic Templates
class IndexView(generic.ListView): # we are going to list data members!
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # Django will manage all the data linking for us
    def get_queryset(self): # we override the built-in get_queryset method
        '''return the last three published questions'''
        return Question.objects.order_by('-pub_date')[:3]

# view for an inherited template (this replicates the 'index' page)
class ChildView(generic.ListView): 
    template_name = 'polls/child.html'
    context_object_name = 'latest_question_list' 
    def get_queryset(self):
        '''return all the questions'''
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView): # this is a detail page!
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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
        selected_weather.wind_speed = request.POST['wind_speed']
        selected_weather.wind_direction = request.POST['wind_direction']
        selected_weather.save()
        weather_list = Weather.objects.order_by('city') 
        context = {'weather_list': weather_list}
        return render(request, 'polls/weather.html', context)
    else:
        # for form has NOT yet been submitted - just show the weather_form view
        weather = get_object_or_404(Weather, pk=weather_id)
        context = {'weather':weather}
        return render(request, 'polls/weather_form.html', context)

