from django import forms
from .models import Questions


class StrokeForm(forms.ModelForm):
    sex = forms.ChoiceField([('0', 'Kobieta'), ('1', 'Mężczyzna')], label='Płeć:', widget=forms.RadioSelect(), initial='0')
    age = forms.ChoiceField( [(n, n) for n in range(55, 85, 1)], label='Wiek', initial='69')
    smoker = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy palisz regularnie papierosy?', initial='0',
                               widget=forms.RadioSelect())
    SBP = forms.ChoiceField([('100', '100'), ('110', '110'), ('120', '120')], label='Ciśnienie skurczowe krwi', initial='100')
    SBP_treatment = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy przyjmujesz leki na nadciśnienie?',
                                      widget=forms.RadioSelect(), initial='0')
    LVH = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na przerost lewej komory?',
                            widget=forms.RadioSelect(), initial='0')
    CVD = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy miałeś/aś w przeszłości problemy z sercem?',
                            widget=forms.RadioSelect(), initial='0')
    AF = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na migotanie przedsionków?',
                           widget=forms.RadioSelect(), initial='0')
    DM = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na cukrzycę?',
                           widget=forms.RadioSelect(), initial='0')
    sleep = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label = 'Czy często się niewysypiasz?',
                           widget=forms.RadioSelect(), initial='0')
    add_question = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś na jeszcze nie wiem co?',
                           widget=forms.RadioSelect(), initial='0')

    class Meta:
        model = Questions
        fields = ('sex', 'age', 'smoker', 'SBP', 'SBP_treatment', 'CVD', 'AF', 'LVH', 'DM')
