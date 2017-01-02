from django.conf import Settings
from django import forms
from django.contrib.admin import widgets
from blog import models


class CommentForm(forms.Form):
    """
    Not sure if I even want comments
    """
    body = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}), label='Comment')
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'textfield'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textfield'}))

    class Meta:
        model = models.Comment
        exclude = ('slug',)
