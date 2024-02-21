from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserRegistrationForm,TransactionForm, CryptocurrencyForm
from .models import Transaction, Cryptocurrency
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
import requests

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('portfolio'))
            return redirect('portfolio')  # Redirect to portfolio page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('portfolio')
    else:
        form = TransactionForm()
    return render(request, 'portfolio/add_transaction.html', {'form': form})

def get_cryptocurrency_price(symbol):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    return data[symbol]['usd']

def add_cryptocurrency(request):
    if request.method == 'POST':
        form = CryptocurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_transaction')
    else:
        form = CryptocurrencyForm()
    return render(request, 'portfolio/add_cryptocurrency.html', {'form': form})



def portfolio(request):
    user_transactions = Transaction.objects.filter(user=request.user)
    total_value = sum(transaction.quantity * transaction.price_per_unit for transaction in user_transactions)
    total_cryptos = user_transactions.count()
    return render(request, 'portfolio/portfolio.html', {'transactions': user_transactions, 'total_value': total_value, 'total_cryptos': total_cryptos})

