from django import forms
from .models import PetArticle

class PetArticleForm(forms.ModelForm):
    class Meta:
        model = PetArticle
        fields = ['title', 'content']
