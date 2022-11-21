from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView # for signup form view
from django.contrib.auth.forms import UserCreationForm  # for signup form
from django.urls import reverse_lazy



# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = ListForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Task Added Successfully !!')
            all_items = List.objects.all()  # List is class name
    else:
        fm = ListForm()
    all_items = List.objects.all()  # List is class name
    return render(request, 'home.html', {'all_items':all_items, 'fm':fm})

def delete(request,list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted!'))
    return redirect('home')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item Has Been Edited!'))
            return redirect('home') # to go other page
    else:
        item = List.objects.get(pk=list_id)
    return render(request, 'edit.html', {'item':item})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

