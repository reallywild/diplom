from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    full_name = forms.CharField(max_length=254, label="ФИО", required=True, widget=forms.TextInput())
    username = forms.CharField(max_length=254, label="Логин", required=True, widget=forms.TextInput())
    password = forms.CharField(max_length=254, min_length=6, label="Пароль", required=True, widget=forms.PasswordInput())
    email = forms.EmailField(max_length=254, label="Почта", required=True, widget=forms.TextInput())

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = 'full_name', 'username', 'password', 'email'



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', max_length=254)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = 'username', 'password'