from django.shortcuts import render
from .models import Book, Author

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

# TODO: Create, modify and delete views for books and libraries (marcalba80) assignment 2


def index(request):
    book = Book.objects.all()

    return render(request, 'generic.html', context={'book':book})


def libros(request):
    book = Book.objects.all().order_by('title')

    return render(request, 'nav/Libros.html', context={'book': book})


def autores(request):
    authors = Author.objects.all().order_by('first_name')
    return render(request, 'nav/Autores.html', context={'autores': authors})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
