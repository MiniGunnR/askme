from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class TimeStamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStamped):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, blank=True, null=True)
    usage = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

class Question(TimeStamped):
    user = models.ForeignKey(User)
    ques = models.CharField('Question', max_length=200)
    desc = models.TextField('Description', default='', blank=True)
    answers = models.PositiveIntegerField('Answer Count', default=0)
    comments = models.PositiveIntegerField('Comment Count', default=0)
    views = models.PositiveIntegerField('View Count', default=0)
    hearts = models.PositiveIntegerField('Heart Count', default=0)
    anon = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    category = models.ForeignKey('Category', default=1)

    def __unicode__(self):
        return self.ques

class Answer(TimeStamped):
    ques = models.ForeignKey('Question')
    user = models.ForeignKey(User)
    ans = models.TextField('Answer')
    comments = models.PositiveIntegerField('Comment Count', default=0)
    views = models.PositiveIntegerField('View Count', default=0)
    hearts = models.PositiveIntegerField('Heart Count', default=0)
    anon = models.BooleanField(default=False)
    not_an_answer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.ans[:100]

class QuestionComment(TimeStamped):
    ques = models.ForeignKey('Question')
    user = models.ForeignKey(User)
    comment = models.TextField('Comment')
    anon = models.BooleanField(default=False)

    def __unicode__(self):
        return self.comment[:100]

class AnswerComment(TimeStamped):
    ans = models.ForeignKey('Answer')
    user = models.ForeignKey(User)
    comment = models.TextField('Comment')
    anon = models.BooleanField(default=False)

    def __unicode__(self):
        return self.comment[:100]

class Stream(TimeStamped):
    type_choices = (
        ('Q', 'Question'),
        ('A', 'Answer'),
    )
    type = models.CharField(max_length=1,
                            choices=type_choices,
                            default='Q')
    ques = models.ForeignKey('Question', blank=True, null=True)
    ans = models.ForeignKey('Answer', blank=True, null=True)

    def __unicode__(self):
        if self.type == 'Q':
            return self.ques.ques
        elif self.type == 'A':
            return self.ans.ans

class Heart(TimeStamped):
    ques = models.ForeignKey('Question', blank=True, null=True)
    ans = models.ForeignKey('Answer', blank=True, null=True)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = (("user", "ques"), ("user", "ans"))
