from django.contrib import admin
from .models import *

@admin.register(Poll)
class PollsAdmin(admin.ModelAdmin):
    fields = ('title', ('start_date', 'finish_date'), 'description', 'questions')
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = ('title', 'question_type', 'visible')

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    fields = ('title', 'question')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    fields = ('user', 'question', 'choice', 'text_answer')

@admin.register(Interviewee)
class IntervieweeAdmin(admin.ModelAdmin):
    fields = ('user', 'custom_id')