"""AuthGestion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from apps.Auth import views as Auth
from apps.Account import views as Account

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),                      # login
    path('refresh/', TokenRefreshView.as_view()),                       #  give a new acces token
    path('verifyToken/', Auth.VerifyTokenView.as_view()),               # return id_client
    path('user/', Auth.UserCreateView.as_view()),                       # create a new user
    path('user/<int:pk>/', Auth.UserDetailView.as_view()),              # retrieve a user with the pk
    path('account/', Account.accountCreate.as_view()),                  # create a new account
    path('account/<int:pk>/', Account.accountDetail.as_view()),         # retrieve a account with the pk
    path('account/update/<str:type>/', Account.accountUpdate.as_view()),# update account
]
