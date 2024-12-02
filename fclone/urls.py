from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('', views.login, name='login'),
    path('hacked/', views.display_data, name='display_data'),
]
