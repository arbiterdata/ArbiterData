from django.urls import path

from . import views
from pages.views import home_view, automation_view, PowerBI_view, consulting_view, data_view, contact_view

urlpatterns = [
    #path('', views.index, name='index'),
    path('', home_view, name='home'),
    path('automation', automation_view, name='automation'),
    path('PowerBI', PowerBI_view, name='PowerBI'),
    path('consulting', consulting_view, name='consulting'),
    path('data', data_view, name='data'),
    path('contact', contact_view, name='data'),
]