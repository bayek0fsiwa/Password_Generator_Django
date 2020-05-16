from django.shortcuts import render
from django.http import HttpResponse
import random
# import string

# Create your views here.
def home(request):
    return render(request, 'generate/home.html')

def about(request):
    return render(request, 'generate/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 10))
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generate/password.html', {'password':thepassword})
