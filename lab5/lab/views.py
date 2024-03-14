from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        new_person = Person(username=username, password=password)
        people.append(new_person)
        return HttpResponseRedirect('/')

    return render(request, 'add.html')

def show_people(request):
    return render(request, 'people.html', {'people': people})

# Create your views here.
