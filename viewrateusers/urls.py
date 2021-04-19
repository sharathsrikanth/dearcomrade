from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewrateuser, name='viewrateuser'),
    path('displayuserdetails/',views.displayuserdetails, name='displayuserdetails'),
    path('saveuserstatus/',views.saveuserstatus, name='saveuserstatus'),
]
