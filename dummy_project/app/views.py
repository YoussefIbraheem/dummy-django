from django.shortcuts import render , redirect

from django.http import HttpResponse
from app.forms import ExampleForm


def register(request):
    return render(request, 'register.html')

def home(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        print(form.data) 
        print(form.errors)
        return redirect('home')
    else:
        form = ExampleForm()
        return render(request, 'index.html', {"form":form})
