from django.urls import path
from . import views

urlpatterns = [
    path('', views.findroommate, name='findroommate'),
    path('displaylist/',views.displaypotentialroommatelist, name='displaylist'),
    path('displayuser/',views.displayuser, name='displayuser'),
]
