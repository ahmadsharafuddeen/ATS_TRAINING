from django.urls import path
from .views import index, book_detail

app_name = 'book_outlet'
urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', book_detail, name='book-detail')
]