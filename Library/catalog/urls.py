from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns =[
    path('',views.index,name='index'),
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
]