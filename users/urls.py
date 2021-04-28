from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('completeuserregistration/', views.completeuserregistration, name='completeuserregistration'),
    path('completeuserprefregistration/', views.completeuserprefregistration, name='completeuserprefregistration'),
    path('completecommunityuserregistration/', views.completecommunityuserregistration, name='completecommunityuserregistration'),
]