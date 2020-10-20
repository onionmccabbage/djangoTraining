from django.contrib import admin

# Register your models here.
from .models import Question
from .models import Weather
from .models import Choice

admin.site.register(Question)
admin.site.register(Weather)
admin.site.register(Choice)