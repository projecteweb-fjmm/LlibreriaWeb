
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('libros/', views.libros, name='libros'),
    path('autores/', views.autores, name='autores'),
    path('book/create', views.BookCreate.as_view(), name='book_create'),
]

