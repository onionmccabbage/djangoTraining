# here we declare the URLs for our polls website
from django.urls import path
from . import views # i.e. from current location

# we can create a namespace for our app 
app_name = 'polls' #(so we can say 'polls:detail' rather than just 'detail')
# declare the patterns we will respond to
urlpatterns = [
    path( '', views.IndexView.as_view(), name='index' ), # here we use generic views i.e. classes cast as views
    path( 'child/', views.ChildView.as_view(), name='child' ),
    path( '<int:pk>/', views.DetailView.as_view(), name='detail'),
    path( '<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path( '<int:question_id>/vote/', views.vote, name='vote' ), # NB vote is never actually visible
    # review 'weather'
    path('weather/', views.weather, name='weather'),
    path('<int:weather_id>/weather_form/', views.weather_form, name='weather_form')
]