from django.shortcuts import render
from .forms import StrokeForm
from django.shortcuts import redirect
from django.http import JsonResponse


def home(request):
    form = StrokeForm()
    context = {'form': form}
    return render(request, 'personal/home.html', context)


def results(request):
    form = StrokeForm(request.POST)
    if not form.is_valid():
        return redirect('/')
    # if this is a POST request we need to process the form data
    # create a form instance and populate it with data from the request:
    result = calculate_result(form)
    form.save()
    # context = {'result': result}
    # return render(request, 'personal/results.html', context)
    return JsonResponse({'result': result})


def calculate_result(form):
    from numpy import exp
    sex = form.instance.sex
    if sex == 0:
        result = (1 - (0.9044 ** (exp(((0.0699*form.instance.age) + (0.0161 * form.instance.SBP) +
                                       (form.instance.SBP_treatment * 0.00026 * (form.instance.SBP - 110) *
                                       (200 - form.instance.SBP)) + (0.4404 * form.instance.CVD) +
                                       (0.8055 * form.instance.LVH) + (0.5419*form.instance.smoker) +
                                       (1.1173 * form.instance.AF) + (0.5604 * form.instance.DM))-7.5766)))) * 100
    else:
        result = (1 - (0.9044 ** (exp(((0.0488*form.instance.age) + (0.0152 * form.instance.SBP) +
                                       (form.instance.SBP_treatment * 0.00019 * (form.instance.SBP - 110) *
                                       (200-form.instance.SBP)) + (0.546 * form.instance.CVD) +
                                       (0.7864 * form.instance.LVH) + (0.5224*form.instance.smoker) +
                                       (0.5998 * form.instance.AF) + (0.3429 * form.instance.DM))-5.6770)))) * 100
    return round(result, 2)
