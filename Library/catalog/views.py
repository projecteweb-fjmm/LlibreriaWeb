from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from .models import Book, Author




from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from catalog.forms import *
from django.views.generic.edit import FormView

# Create your views here.

def index(request):
    book = Book.objects.all()

    return render(request, 'generic.html', context={'book':book})


def libros(request):
    book = Book.objects.all().order_by('title')

    return render(request, 'nav/Libros.html', context={'book': book})


def autores(request):
    autores = Author.objects.all().order_by('first_name')
    return render(request, 'nav/Autores.html', context={'autores': autores})

class BookCreate(LoginRequiredMixin,generic.CreateView):
    template_name = 'changes/CreateBook.html'
    model = Book
    form_class = BookForm
    success_url = '/all_books'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BookCreate,self).form_valid(form)

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

class BookUpdate(LoginRequiredMixin,generic.UpdateView):
    template_name = 'changes/UpdateBook.html'
    model = Book
    fields = '__all__'

class BookDelete(LoginRequiredMixin,generic.DeleteView):
    template_name = 'changes/DeleteBook.html'
    model = Book
    success_url = reverse_lazy('index')
