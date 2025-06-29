from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(label="News about", max_length=50)
