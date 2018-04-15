from django import forms
import datetime

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class EventForm(forms.Form):
    title = forms.CharField(max_length =200)
    description = forms.CharField(widget=forms.Textarea())
    location = forms.CharField(max_length=200)
    date = forms.DateTimeField(widget=forms.DateTimeInput())
    attended_or_not = forms.CharField(max_length=20)