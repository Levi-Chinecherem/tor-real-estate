from django.urls import path
from . import views

urlpatterns = [
    path('application/', views.buyer_application, name='buyer_application'),
    path('buy/<int:land_id>/', views.buy_land, name='buy_land'),
]
