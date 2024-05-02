from django.urls import path
from contact import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('search/', views.search, name='search'),
    path('contact/<int:contact_id>/update/', views.update, name='update'),
]