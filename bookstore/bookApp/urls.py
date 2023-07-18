from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),
path('book/<int:id>/', views.book, name='book'),
 
path('category/<id>/', views.category, name="category"),
path('aboutus/', views.aboutus, name='aboutus'),
path('books/', views.books, name="books"),
path('contact/', views.contact, name="contact"),
path('subscribe/', views.subscribe, name='subscribe'),
path('search/', views.search, name='search'),


]
