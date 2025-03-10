from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('/notes/', permanent=True)),  # Redirect to /notes/
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add built-in auth views
    path('notes/', include('notes.urls')),
]