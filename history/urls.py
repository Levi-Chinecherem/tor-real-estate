from django.urls import path
from . import views

urlpatterns = [
    path('user-history/', views.user_history, name='user_history'),
    path('land-history/', views.land_history, name='land_history'),
]
