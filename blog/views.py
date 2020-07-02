from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    return render(request, 'Website/home.html')

def tintuc(request):
    return render(request, 'Website/tin-tuc.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()



