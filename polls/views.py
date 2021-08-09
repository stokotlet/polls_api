from .serializers import QuestionSerializer, PollSerializer, PollListSerializer, AnswerSerializer
from rest_framework import permissions
from rest_framework import generics
from .models import Question, Poll, Answer
from datetime import date


class PollsListView(generics.ListAPIView):
    queryset = Poll.objects.filter(start_date__lte=date.today())
    permission_classes = (permissions.AllowAny,)
    serializer_class = PollListSerializer

class PollsDetailView(generics.RetrieveAPIView):
    queryset = Poll.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PollSerializer

class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = QuestionSerializer

class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerRetrieveView(generics.RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
