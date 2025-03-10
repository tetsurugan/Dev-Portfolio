from django.contrib import admin
from django.urls import path, include
from expenses.views import expense_list  # Import list view

urlpatterns = [
    path('', expense_list, name='home'),  # Redirect root to expenses list
    path('admin/', admin.site.urls),
    path('expenses/', include('expenses.urls')),  # Include app routes
]