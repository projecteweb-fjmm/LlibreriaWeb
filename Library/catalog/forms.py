from django.forms import ModelForm
from catalog.models import Book,Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ('user',)

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        exclude = ('user',)