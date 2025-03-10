from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),  # Make sure there's a valid view here
    path('register/', views.register, name='register'),
    path('new/', views.new_note, name='new_note'),
    path('<int:id>/edit/', views.edit_note, name='edit_note'),
    path('<int:id>/delete/', views.delete_note, name='delete_note'),
    path('search/', views.search_notes, name='search_notes'),
]