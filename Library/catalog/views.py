from django.shortcuts import render
from  .models import *

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.

def index(request):
    book = Book.objects.all()

    return render(request, 'generic.html',context={'book':book})

def libros(request):
    book = Book.objects.all()
    return render(request, 'Nav/Libros.html', context={'book': book})

def autores(request):
    autores = Author.objects.all()
    return render(request, 'Nav/Autores.html', context={'autores': autores})