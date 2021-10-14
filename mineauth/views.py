from django.shortcuts import render
from django.contrib.auth.views import LoginView


class LoginView(LoginView):
	redirect_url = '/authorize'

# Create your views here.
