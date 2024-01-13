from django.urls import path
from . import views
urlpatterns=[
    path('booklist',views.home,name='books'),
    path('booklist/<int:id>',views.get_book,name='book')
]