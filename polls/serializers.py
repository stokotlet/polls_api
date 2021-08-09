from rest_framework import serializers
from .models import Answer, Question, Choice, Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'
        depth = 3


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        exclude = ['questions']


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    question_type = serializers.ChoiceField(choices=Question.Type.QUESTION_TYPES, default=Question.Type.text)

    class Meta:
        model = Question
        fields = ['title', 'question_type', 'choice_set']
        depth = 1

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'