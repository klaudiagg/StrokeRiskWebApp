from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import Question

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'personal/home.html', context)


def results(request):
    return render(request, 'personal/results.html')
