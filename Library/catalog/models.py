from django.db import models
from django.urls import reverse


from django.contrib.auth.models import User

import uuid

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Write a genre for example 'Adventures'")

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=32, help_text="Introduce Language")

    def __str__(self):
        return self.language


class Author(models.Model):
    first_name = models.CharField(max_length=32)

    second_name = models.CharField(max_length=32)

    native_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True,
                                           help_text="Choose a language")

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '%s  %s' % (self.first_name, self.second_name)

    def get_absolute_url(self):
        return reverse('author_detail', args=[str(self.id)])


class Book (models.Model):

    title = models.CharField(max_length=128, help_text="Write the title of the book")

    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)

    summary = models.TextField(max_length=500, help_text="Write a brief summary of the book")

    isbn = models.CharField('ISBN', max_length=13, help_text="Write ISBN, 13 Characters")

    genre = models.ManyToManyField(Genre, help_text="Choose the genre")

    language = models.ManyToManyField(Language, help_text="Choose the language")

    date_published = models.DateField(null=True)

    picture = models.ImageField(default="default.png", null=False)

    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class BookInstance (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Asigna un ID unico para este libro en toda la biblioteca")

    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    editorial = models.CharField(max_length=256)

    due_back = models.DateField(null=True)

    LOAN_STATUS = (('m', 'Mantenimiento'), ('p', 'Prestado'), ('d', 'Disponible'), ('r', 'Reservado'))

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                              help_text="Disponibility of the book")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return 'ID: %s - Title: %s' % (self.id, self.book.title)


class Library(models.Model):

    address = models.CharField(max_length=64, help_text="Put the direction")

    postal_code = models.CharField(max_length=5, help_text="Put the postal code")

    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    lon = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return 'ZIP: %s - Addrress: %s' % (self.postal_code, self.address)

