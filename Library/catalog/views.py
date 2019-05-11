from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from .models import Book, Author
from django.core.exceptions import PermissionDenied
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from catalog.forms import *


# Security Mixin
class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj


# Create your views here.

def index(request):
    book = Book.objects.all().order_by('-date_published')

    return render(request, 'generic.html', context={'book':book})


def libros(request):
    book = Book.objects.all().order_by('title')

    return render(request, 'nav/Libros.html', context={'book': book})


def autores(request):
    autores = Author.objects.all().order_by('first_name')
    return render(request, 'nav/Autores.html', context={'autores': autores})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class BookDetailView(generic.DetailView):
    template_name = 'catalog/book_detail.html'
    model = Book

class AuthorDetailView(generic.DetailView):
    template_name = 'catalog/author_detail.html'
    model = Author

class BookCreate(LoginRequiredMixin,generic.CreateView):
    template_name = 'changes/Create.html'
    model = Book
    form_class = BookForm
    success_url = '/all_books'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate,self).form_valid(form)

class BookUpdate(LoginRequiredMixin,CheckIsOwnerMixin,generic.UpdateView):
    template_name = 'changes/UpdateBook.html'
    model = Book
    fields = ['title','author','summary','isbn','genre','language','date_published','picture']

class BookDelete(LoginRequiredMixin,CheckIsOwnerMixin,generic.DeleteView):
    template_name = 'changes/DeleteBook.html'
    model = Book
    success_url = reverse_lazy('all_books')

class AuthorCreate(LoginRequiredMixin,generic.CreateView):
    template_name = 'changes/Create.html'
    model = Author
    form_class = AuthorForm
    success_url = '/author'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AuthorCreate,self).form_valid(form)

class AuthorUpdate(LoginRequiredMixin,CheckIsOwnerMixin,generic.UpdateView):
    template_name = 'changes/UpdateAuthor.html'
    model = Author
    fields = ['first_name','second_name','native_language']

class AuthorDelete(LoginRequiredMixin,CheckIsOwnerMixin,generic.DeleteView):
    template_name = 'changes/DeleteAuthor.html'
    model = Author
    success_url = reverse_lazy('author')



