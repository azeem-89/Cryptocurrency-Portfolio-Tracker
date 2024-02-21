from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cryptocurrency, Transaction
from django import forms

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['cryptocurrency', 'quantity', 'price_per_unit']

class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = ['name', 'symbol']