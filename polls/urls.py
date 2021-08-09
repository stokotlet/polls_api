from django.urls import path, include
from .views import PollsListView, PollsDetailView, QuestionDetailView, AnswerCreateView, AnswerRetrieveView

urlpatterns = [
    path('polls/', PollsListView.as_view(), name='polls'),
    path('polls/<int:pk>', PollsDetailView.as_view(), name='poll_detail'),
    path('questions/<int:pk>', QuestionDetailView.as_view(), name='question_detail'),
    path('answer/', AnswerCreateView.as_view(), name='answer_create'),
    path('answer/<int:pk>', AnswerRetrieveView.as_view(), name='answer_detail')

    ]