from django import forms
from .models import Questions


class StrokeForm(forms.ModelForm):
    sex = forms.ChoiceField([('0', 'Kobieta'), ('1', 'Mężczyzna')], label='Płeć:', widget=forms.RadioSelect())
    age = forms.ChoiceField([(n, n) for n in range(55, 85, 1)], label='Wiek', initial='55')
    smoker = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy palisz regularnie papierosy?',
                               widget=forms.RadioSelect())
    SBP = forms.ChoiceField([(n, n) for n in range(95, 216, 5)], label='Ciśnienie skurczowe krwi', initial='95')
    SBP_treatment = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy przyjmujesz leki na nadciśnienie?',
                                      widget=forms.RadioSelect())
    LVH = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na przerost lewej komory?',
                            widget=forms.RadioSelect())
    CVD = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy miałeś/aś w przeszłości problemy z sercem?',
                            widget=forms.RadioSelect())
    AF = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na migotanie przedsionków?',
                           widget=forms.RadioSelect())
    DM = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na cukrzycę?',
                           widget=forms.RadioSelect())
    sleep = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy często się niewysypiasz?',
                              widget=forms.RadioSelect())
    add_question2 = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś na jeszcze nie wiem co?',
                                      widget=forms.RadioSelect())

    class Meta:
        model = Questions
        fields = ('sex', 'age', 'smoker', 'SBP', 'SBP_treatment', 'CVD', 'AF', 'LVH', 'DM', 'sleep', 'add_question2')
