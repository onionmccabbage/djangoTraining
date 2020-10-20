# here we declare the URLs for our polls website
from django.urls import path
from . import views # i.e. from current location

# we can create a namespace for our app 
app_name = 'polls' #(so we can say 'polls:detail' rather than just 'detail')
# declare the patterns we will respond to
urlpatterns = [
    path('', views.index, name='index'), # our first routing path
    path('weather/', views.weather, name='weather'),
    # ex /polls/5/ NB all URL values are STRING so we cast as int where needed
    path('<int:question_id>/', views.detail, name='detail'), # <> allow for a parameter
    # ex /polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('demo_form/', views.demo_form, name='DemoForm')
]