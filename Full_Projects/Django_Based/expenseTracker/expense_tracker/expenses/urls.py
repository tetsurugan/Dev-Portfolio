from django.contrib import admin
from django.urls import path, include
from .views import add_expense, expense_list, delete_expense, ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('admin/', admin.site.urls),  # Corrected admin path
    path('', expense_list, name='expense_list'),  # Home redirects to the expense list
    path('add/', add_expense, name='add_expense'),
    path('list/', expense_list, name='expense_list'),
    path('api/', ExpenseListCreateView.as_view(), name='expense_api_list_create'),
    path('api/<int:pk>/', ExpenseDetailView.as_view(), name='expense_api_detail'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
]