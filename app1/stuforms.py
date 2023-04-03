from django import forms
from django.forms import ModelForm
from .models import stud
#class StudForm(forms.Form):

class StudForm(ModelForm):
    class Meta:
        model=stud
        fields='__all__'
    # s_name=forms.CharField(max_length=30)
    # s_class=forms.CharField(max_length=30)
    # s_addr=forms.CharField(max_length=30)
    # s_school=forms.CharField(max_length=30)
    # s_email=forms.EmailField(max_length=30)
class SrchForm(forms.Form):
    s_name=forms.CharField(max_length=30)
