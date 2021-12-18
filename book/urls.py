from book import views
from django.urls import path

urlpatterns=[
    path('', views.index, name="index_book"),
    path('create/', views.create_book, name="create_book"),
    path('update/<int:book_id>', views.update_book, name="update_book"),
    path('delete/<int:book_id>', views.delete_book, name="delete_book"),
]