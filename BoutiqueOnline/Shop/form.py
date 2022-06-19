from django import forms
from .models import BlogPost

JOB =(
    ("python", "Deveppeur en python"),
    ("JavaScript", "Developpeur en javascript"),
    ("PHP", "Developpeur en php")
)


class Formulaire(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=5)
    jod = forms.ChoiceField(choices=JOB)
    cgu_accept = forms.BooleanField(initial=True)


    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("le pseudo ne pas contenir un dollard")
        return pseudo


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "author","published", "content"]