from django.contrib import admin

# Register your models here.
from .models import Question, QuestionOption, TestingKit, TestingResult, TestingUser

admin.site.register(Question)
admin.site.register(QuestionOption)
admin.site.register(TestingKit)
admin.site.register(TestingResult)
admin.site.register(TestingUser)
