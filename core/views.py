
# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
  return render(request, 'login.html')
  
@login_required
def home(request):
  social = request.user.social_auth.get(provider='facebook')
  token = social.extra_data['access_token']
  return render(request, 'home.html', context={'token':token})