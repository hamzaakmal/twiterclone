from dataclasses import field
from pdb import post_mortem
from django import forms
from .models import Post


class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
