from django.urls import path
from . import views

urlpatterns = [
    # Modify the path for the index view to include both '' and 'inicio'
    path('', views.index, name='index'),
    path('inicio/', views.index, name='inicio'),  # Add a trailing slash for consistency
    # Keep the path for the login view unchanged
    path('login/', views.login_view, name='login'),
]
