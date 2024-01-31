from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.book_list, name = 'book_list'),
    path('find/', views.book_search, name = 'book_search'),
    path('<slug:slug>/', views.book_details, name = 'book_details'),
]