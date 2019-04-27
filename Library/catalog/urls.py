
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('all_books/', views.libros, name='all_books'),
    path('author/', views.autores, name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('book/create', views.BookCreate.as_view(), name='book_create'),
    path('book/update/<int:pk>', views.BookUpdate.as_view(), name='book_update'),
    path('book/delete/<int:pk>', views.BookDelete.as_view(), name='book_delete'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
]

