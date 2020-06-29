from django.shortcuts import render
from .models import Finch
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# class Finch:  # Note that parens are optional if not inheriting from another class
#     def __init__(self, name, breed, description, age):
#         self.name = name
#         self.breed = breed
#         self.description = description
#         self.age = age


# finches = [
#     Finch('Lolo', 'tabby', 'foul little demon', 3),
#     Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
#     Finch('Raven', 'black tripod', '3 legged cat', 4)
# ]

# Define the home view


def home(request):
    return render(request, 'home.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})


class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'scientific_name', 'mass', 'length']


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['scientific_name', 'mass', 'length']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
