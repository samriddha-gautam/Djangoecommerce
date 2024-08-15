
from django import forms
from students.models import College

class StudentForm(forms.Form):
    rollNO = forms.IntegerField()
    name = forms.CharField(max_length=100)
    address= forms.CharField(max_length=50)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    college = forms.ModelChoiceField(queryset=College.objects.all(), empty_label="Select college",to_field_name='id')

    