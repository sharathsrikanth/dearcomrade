from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class CommunityDetails (models.Model):
    communityid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=250)
    addr2 = models.CharField(max_length=250)
    phnumber = models.CharField(max_length=11)
    description = models.CharField(max_length=500)
    avgrent = models.CharField(max_length=500)
    communitypictureurl = models.CharField(max_length=2083)

    class Meta:
       db_table = 'communitydetails'

    def __str__(self):
        return str(self.communityid)

class CommunityUserDetails (models.Model):
    communityid = models.ForeignKey(CommunityDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    communityuserid = models.CharField(max_length=50)

    class Meta:
       unique_together = (("communityuserid", "name"),)
       db_table = 'communityuserdetails'

    def __str__(self):
        return (str(self.name))


