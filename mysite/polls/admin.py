from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Weather
from .models import Choice

# delare a class to 'inline' the choices along with the question
class ChoiceInline(admin.StackedInline):
    model = Choice
    # we can choose how many to show by default
    extra = 3

# declare a class to customize the Question admin
class QuestionAdmin(admin.ModelAdmin):
    # we can specify the order of the form fields
    # fields = ['pub_date', 'question_text']
    # .. or group fields together in field sets
    fieldsets= [
                (None, {'fields':['question_text']}),
                ('Date info', {'fields':['pub_date'], 'classes':['collapse']}),
               ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin) # register our admin class
admin.site.register(Weather)
# We no longer register 'choice' as a separate form
# admin.site.register(Choice)