from django.urls import path
from . import views

urlpatterns = [
    path('', views.findcommunities, name='findcommunities'),
    path('displaycommunity/',views.displaycommunity, name='displaycommunity'),
]
