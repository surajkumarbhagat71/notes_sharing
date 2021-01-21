from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator


class UserRegistationForm(UserCreationForm):
    email = forms.EmailField(label='email',validators=[EmailValidator],error_messages={"invalid":'This is invalid email address'})
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']



class AddProfileDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        exclude = ('user',)



class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteShare
        exclude = ('sender_id','reciver_id')
