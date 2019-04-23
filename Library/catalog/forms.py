from django.forms import ModelForm
from catalog.models import Book, Library

# code from myrecommendations rogargon


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('user', 'date', 'library',)


class LibraryForm(ModelForm):
    class Meta:
        model = Library
        exclude = ('user', 'date',)
