from django import forms
from app.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "excerpt", "content", "author", "category", "status"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "excerpt": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "author": forms.Select(attrs={"class": "form-select"}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }
