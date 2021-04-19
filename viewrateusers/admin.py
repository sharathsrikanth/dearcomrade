from django.contrib import admin
from .models import Usersdata, Userpreference, UserRating


class UsersdataAdmin(admin.ModelAdmin):
    list_display = ('userid', 'fname', 'lname', 'phnumber', 'age', 'sex', 'addr1', 'addr2', 'country', 'description', 'workinfo', 'profilepicurl')


class UserpreferenceAdmin(admin.ModelAdmin):
    list_display = ('userid', 'prefid', 'cleanliness', 'booze_smoke', 'prefapartment1','prefapartment2','prefapartment3')


class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('userid', 'ratingid', 'peerrating', 'guestrating', 'communityrating')


admin.site.register(Usersdata,UsersdataAdmin)
admin.site.register(Userpreference, UserpreferenceAdmin)
admin.site.register(UserRating, UserRatingAdmin)
