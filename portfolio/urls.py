from django.urls import path
from .views import register, user_login,portfolio,add_transaction, add_cryptocurrency

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('portfolio/', portfolio, name='portfolio'),
    path('add_transaction/',add_transaction,name= 'add_transaction'),
    path('add-cryptocurrency/', add_cryptocurrency, name='add_cryptocurrency'),

]
