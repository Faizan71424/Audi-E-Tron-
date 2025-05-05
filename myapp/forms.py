from django import forms


class postt(forms.Form):
    title = forms.CharField()
    blog=forms.CharField()