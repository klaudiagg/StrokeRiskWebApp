from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponse
from .models import Question, Choice
from .forms import HomeForm


def home(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()
    form = HomeForm()
    context = {'questions': questions, 'choices': choices, 'form': form}
    return render(request, 'personal/home.html', context)


# def results(request):
#    return render(request, 'personal/results.html')

'''def results(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST
        print(form)

    return render(request, 'personal/results.html', {'form': form})
'''


def results(request):
    # if this is a POST request we need to process the form data
    # create a form instance and populate it with data from the request:
    return render(request, 'personal/results.html')
