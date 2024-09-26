from django import forms
from .models import UserAccount

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserAccount
        fields = ('email', 'password', 'first_name', 'last_name')

    def clean_password(self):
        return self.cleaned_data['password']
