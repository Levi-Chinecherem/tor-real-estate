from django.urls import path
from .views import confirmed_lands, my_properties, unconfirmed_lands, land_detail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('confirmed/', confirmed_lands, name='confirmed_lands'),
    path('unconfirmed/', unconfirmed_lands, name='unconfirmed_lands'),
    path('<int:land_id>/', land_detail, name='land_detail'),
    path('my-properties/', my_properties, name='my_properties'), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
