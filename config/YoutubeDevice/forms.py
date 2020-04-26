from django import forms
from django.contrib.auth.models import User
from .models import Card


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title","description","streamer","pic_path","youtube_channel","device1","device1_spec","device2","device2_spec","gametitle","user",)
