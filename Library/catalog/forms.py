from django.forms import ModelForm
from catalog.models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)