from django.contrib import admin
from .models import CommunityDetails


class CommunitydataAdmin(admin.ModelAdmin):
    list_display = ('communityid', 'name', 'addr1', 'addr2', 'phnumber', 'description', 'avgrent', 'communitypictureurl')

admin.site.register(CommunityDetails,CommunitydataAdmin)