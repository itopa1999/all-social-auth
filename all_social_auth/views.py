from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import Group, User
# Create your views here.


def index(request):
    try:
        news = User.objects.filter(email = request.user.email)
    except:
        news = User.objects.filter(email = '123222222222@gmail.com')
    messages.success(request, 'hello this is required')
    return render(request, 'index.html')