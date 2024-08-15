from django import forms
from django.contrib.auth import authenticate

class userLoginForm(forms.form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

def __init__(self, *args, **kwargs):
    super(userLoginForm, self).__init__(*args, **kwargs)
    self.fiels['username'].widget.attrs.update({
        'class': 'form-control',
        'name': 'username'})
    self.fields['password'].widget.attrs.update({
        'class':'form-control',
        'name': 'password'})

def clean(self,*args,**kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    if username and password:
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password')
        elif not user.check_password(password):
            raise forms.ValidationError('User doesnt exists')
    return super(userLoginForm,self).clean(*args, **kwargs)    