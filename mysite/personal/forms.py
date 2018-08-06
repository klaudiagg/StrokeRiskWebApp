from django import forms
from .models import Questions


class HomeForm(forms.ModelForm):
    sex = forms.ChoiceField([('female', 'Kobieta'), ('male', 'Mężczyzna')], label='Płeć:', widget=forms.RadioSelect())
    age = forms.ChoiceField([('64', '64'), ('65', '65'), ('66', '66')], label='Wiek')
    smoker = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy palisz regularnie papierosy?',
                               widget=forms.RadioSelect())
    SBP = forms.ChoiceField([('100', '100'), ('110', '110'), ('120', '120')], label='Ciśnienie skurczowe krwi')
    SBP_treatment = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy przyjmujesz leki na nadciśnienie?',
                                      widget=forms.RadioSelect())
    LVH = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na przerost lewej komory?',
                            widget=forms.RadioSelect())
    CVD = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy miałeś/aś w przeszłości problemy z sercem?',
                            widget=forms.RadioSelect())
    AF = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na migotanie przedsionków',
                           widget=forms.RadioSelect())
    DM = forms.ChoiceField([('1', 'Tak'), ('0', 'Nie')], label='Czy chorowałeś kiedykolwiek na cukrzycę',
                           widget=forms.RadioSelect())

    class Meta:
        model = Questions
        fields = ('sex', 'age', 'smoker', 'SBP', 'SBP_treatment', 'CVD', 'AF', 'LVH', 'DM')
