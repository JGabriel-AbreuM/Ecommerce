from django import forms
from django.contrib.auth import get_user_model

class SignupForm(forms.Form):
    CHOICES = (
        ("VD", ("Vendedor")),
        ("CP", ("Comprador"))
    )

    type = forms.ChoiceField(choices=CHOICES, label="Tipo")  

    def signup(self, request, user):
        user.type = self.cleaned_data["type"]
        user.save()

