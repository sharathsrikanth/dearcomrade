from django.db import models


class CommunityDetails (models.Model):
    communityid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=250)
    addr2 = models.CharField(max_length=250)
    phnumber = models.IntegerField()
    description = models.CharField(max_length=500)
    avgrent = models.CharField(max_length=500)
    communitypictureurl = models.CharField(max_length=2083)

    class Meta:
       db_table = 'communitydetails'

    def __str__(self):
        return str(self.communityid)

