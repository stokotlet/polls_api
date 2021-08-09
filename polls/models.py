from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    class Type:
        text = 'text'
        single_choice = 'single_choice'
        multi_choice = 'multi_choice'
        QUESTION_TYPES = (
            (text, 'text'),
            (single_choice, 'single_choice'),
            (multi_choice, 'multi_choice')
            )

    title = models.CharField(max_length=4096)
    question_type = models.CharField(max_length=50, choices=Type.QUESTION_TYPES)
    visible = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Poll(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    finish_date = models.DateField()
    description = models.TextField()
    questions = models.ManyToManyField(Question)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is not None:
            self.start_date = Poll.objects.get(id=self.pk).start_date
        return super(Poll, self).save()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField(max_length=4096)

    def __str__(self):
        return self.title


class Interviewee(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    custom_id = models.IntegerField(unique=True)


class Answer(models.Model):
    user = models.ForeignKey(Interviewee, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    text_answer = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.choice.title
