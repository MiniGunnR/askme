from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from .models import Stream, Question, Answer, Heart

class StreamListView(ListView):
    model = Stream
    template_name = 'qna/stream.html'
    context_object_name = 'stream'
    ordering = '-created'

# class PopularListView(ListView):
#     model = Question
#     template_name = 'qna/stream.html'
#     context_object_name = 'stream'
#     ordering = ['hearts', 'answers']

class PostDetailView(DetailView):
    model = Stream
    template_name = 'qna/post.html'

def HeartView(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    try:
        if stream.ques:
            Heart.objects.create(ques=stream.ques, user=request.user)
        elif stream.ans:
            Heart.objects.create(ans=stream.ans, user=request.user)
        return JsonResponse({
            "message": "OK"
        })
    except IntegrityError as e:
        return JsonResponse({
            "error": e.message,
            "message": "The current user has already hearted this post."
        })

def UnheartView(request, pk):
    stream = get_object_or_404(Stream, pk=pk)
    try:
        if stream.ques:
            Heart.objects.get(ques=stream.ques, user=request.user).delete()
        elif stream.ans:
            Heart.objects.get(ans=stream.ans, user=request.user).delete()
        return JsonResponse({
            "message": "OK"
        })
    except ObjectDoesNotExist:
        return JsonResponse({
            "message": "Cannot unheart post that has not been hearted."
        })
