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
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verifyToken/', Auth.VerifyTokenView.as_view()),
    path('user/', Auth.UserCreateView.as_view()),
    path('user/<int:pk>/', Auth.UserDetailView.as_view()),
    path('account/', Account.accountCreate.as_view()),
    path('account/<int:pk>/', Account.accountDetail.as_view()),
    path('account/update/<str:type>/', Account.accountDetail.as_view()),
]
