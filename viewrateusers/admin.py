from django.contrib import admin
from .models import Usersdata, Userpreference, UserRating, UserHistory, UserPeerTagging, UserComments


class UsersdataAdmin(admin.ModelAdmin):
    list_display = ('userid', 'fname', 'lname', 'phnumber', 'age', 'sex', 'addr1', 'addr2', 'country', 'description', 'workinfo', 'profilepicurl')


class UserpreferenceAdmin(admin.ModelAdmin):
    list_display = ('userid', 'prefid', 'cleanliness', 'booze_smoke', 'prefapartment1','prefapartment2','prefapartment3')


class UserRatingAdmin(admin.ModelAdmin):
    list_display = ('userid', 'ratingid', 'peerrating', 'guestrating', 'communityrating')


class UserHistoryAdmin(admin.ModelAdmin):
    list_display = ('userid', 'userhistoryid', 'prevapartment1', 'prevapartment2', 'prevapartment3')


class UserPeerTaggingAdmin(admin.ModelAdmin):
    list_display = ('communityid', 'aptno', 'userid1', 'userid2', 'userid3', 'userid4')


class UserCommentsAdmin(admin.ModelAdmin):
    list_display = ('userid', 'commentid', 'comment')


admin.site.register(Usersdata,UsersdataAdmin)
admin.site.register(Userpreference, UserpreferenceAdmin)
admin.site.register(UserRating, UserRatingAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
admin.site.register(UserPeerTagging, UserPeerTaggingAdmin)
admin.site.register(UserComments, UserCommentsAdmin)