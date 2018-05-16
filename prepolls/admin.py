from django.contrib import admin
from .models import Question, Choice, PreVoter

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PreVoter)