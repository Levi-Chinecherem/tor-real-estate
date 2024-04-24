from django.urls import path
from . import views


urlpatterns = [
    path('apply/', views.seller_application, name='seller_application'),
    path('upload/', views.land_upload, name='land_upload'),
]
