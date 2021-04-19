from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dearcomradehome'),
    #path('findroommate/', views.about, name='dearcomradeaboutabout'),
    #path('')
]
