from django import forms
from app.models import Article

class ArticleForm(forms.Form):
    
    title = forms.CharField(max_length=200, required=True, label='Article Title', widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(required=True, label='Content',widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    author = forms.CharField(max_length=100, required=True, label='Author Name', widget=forms.TextInput(attrs={"class": "form-control"}))