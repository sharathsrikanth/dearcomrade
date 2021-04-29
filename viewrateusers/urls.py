from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewrateuser, name='viewrateuser'),
    path('displayuserdetails/',views.displayuserdetails, name='displayuserdetails'),
    path('addcommentratings/',views.addcommentratings, name='addcommentratings'),
    path('displayuser/',views.searchusers, name='searchusers'),
    path('saveuserstatus/',views.saveuserstatus, name='saveuserstatus'),
    path('saveuserprofilepicture/',views.saveuserprofilepicture, name='saveuserprofilepicture'),
]
