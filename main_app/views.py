from django.shortcuts import render,redirect
from .models import Finch, Tree
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SeenForm

def home(request):
    return render(request, 'home.html')


def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})


def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    trees_havnt_seen = Tree.objects.exclude(id__in=finch.trees.all().values_list('id'))
    seen_form = SeenForm()
    return render(request, 'finches/detail.html', {'finch': finch,'seen_form':seen_form,'tree':trees_havnt_seen})

def add_seen(request,finch_id):
    form = SeenForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save the form to the db until it
        # has the cat_id assigned
        new_seen = form.save(commit=False)
        new_seen.finch_id = finch_id
        new_seen.save()
    return redirect('detail', finch_id=finch_id)

def assoc_tree(request, finch_id, tree_id):
    Finch.objects.get(id=finch_id).trees.add(tree_id)
    return redirect('detail',finch_id=finch_id)

class FinchCreate(CreateView):
    model = Finch
    fields = ['name', 'scientific_name', 'mass', 'length']


class FinchUpdate(UpdateView):
    model = Finch
    fields = ['scientific_name', 'mass', 'length']


class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches/'
