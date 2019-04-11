from django.db import models
from django.urls import reverse
# from django.contrib.gis.db import models #GEODJANGO MODEL API

import uuid

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Escribe un genero literario e.j: Aventuras")

    def __str__(self):
        return self.name


class Language(models.Model):
    language = models.CharField(max_length=32, help_text="Escribe un idioma")

    def __str__(self):
        return self.language


class Author(models.Model):
    first_name = models.CharField(max_length=32)

    second_name = models.CharField(max_length=32)

    native_language = models.OneToOneField(Language, on_delete=models.SET_NULL, null=True,
                                           help_text="Selecciona el lenguage nativo de escritura del autor")

    def __str__(self):
        return '%s  %s' % (self.first_name, self.second_name)


class Book (models.Model):

    title = models.CharField(max_length=128, help_text="Escribe el titulo del libro que desea guardar e.j: THE 100")

    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)

    summary = models.TextField(max_length=500, help_text="Escribe un breve resumen del libro")

    isb = models.CharField('ISBN', max_length=13, help_text="Escribe un ISBN valido (13 caracteres)")

    genre = models.ManyToManyField(Genre, help_text="Selecciona un genero literario")

    language = models.ManyToManyField(Language, help_text="Selecciona los idiomas que esta escrito el libro")

    date_published = models.DateField(null=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    def get_absolute_url(self):

        return reverse('book-detail', args=[str(self.id)])


class BookInstance (models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,
                          help_text="Asigna un ID unico para este libro en toda la biblioteca")

    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)

    editorial = models.CharField(max_length=256)

    due_back = models.DateField(null=True)

    LOAN_STATUS = (('m', 'Mantenimiento'), ('p', 'Prestado'), ('d', 'Disponible'), ('r', 'Reservado'))

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m',
                              help_text="Disponibilidad del libro")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return 'ID: %s - Title: %s' % (self.id, self.book.title)


class Library(models.Model):

    address = models.CharField(max_length=64, help_text="Inserte la direccion")

    postal_code = models.CharField(max_length=5, help_text="Inserte el codigo postal")

    lat = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    lon = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)

    def __str__(self):
        return 'ZIP: %s - Addrress: %s' % (self.postal_code, self.address)
