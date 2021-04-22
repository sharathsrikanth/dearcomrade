from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from community.models import CommunityDetails


class Usersdata (models.Model):
    userid = models.CharField(max_length=50, primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phnumber = models.IntegerField()
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    addr1 = models.CharField(max_length=250)
    addr2 = models.CharField(max_length=250)
    country = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    workinfo = models.CharField(max_length=500)
    profilepicurl = models.CharField(max_length=2083)

    class Meta:
       db_table = 'usersdata'

    def __str__(self):
        return self.userid


class Userpreference (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    prefid = models.IntegerField()
    preflocation = models.CharField(max_length=50)
    prefsex = models.CharField(max_length=10)
    usersex = models.CharField(max_length=10)
    budget = models.IntegerField()
    cleanliness = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    booze_smoke = models.BooleanField(default=False)
    prefapartment1 = models.CharField(max_length=50)
    prefapartment2 = models.CharField(max_length=50)
    prefapartment3 = models.CharField(max_length=50)
    statusavailable = models.BooleanField(default=True, null=True)

    class Meta:
        unique_together = (("userid", "prefid"),)
        db_table = 'userpreference'

    def __str__(self):
        return str(self.userid)


class UserRating (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    ratingid = models.IntegerField()
    peerrating = models.FloatField( validators=[MaxValueValidator(5), MinValueValidator(0)])
    guestrating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])
    communityrating = models.FloatField(validators=[MaxValueValidator(5), MinValueValidator(0)])

    class Meta:
        unique_together = (("userid", "ratingid"),)
        db_table = 'userrating'

    def __str__(self):
        return str(self.userid)


class UserComments (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    commentid = models.IntegerField()
    comment = models.CharField(max_length = 3000)

    class Meta:
        unique_together = (("userid", "commentid"),)
        db_table = 'usercomments'

    def __str__(self):
        return self.userid


class UserHistory (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    userhistoryid = models.IntegerField()
    prevapartment1 = models.CharField(max_length=50)
    prevapartment2 = models.CharField(max_length=50)
    prevapartment3 = models.CharField(max_length=50)

    class Meta:
        unique_together = (("userid", "userhistoryid"),)
        db_table = 'userhistory'

    def __str__(self):
        return str(self.userid)


class UserPeerTagging (models.Model):
    communityid = models.ForeignKey(CommunityDetails, on_delete=models.CASCADE)
    aptno = models.IntegerField()
    userid1 = models.CharField(max_length=50)
    userid2 = models.CharField(max_length=50)
    userid3 = models.CharField(max_length=50)
    userid4 = models.CharField(max_length=50)

    class Meta:
        unique_together = (("communityid", "aptno"),)
        db_table = 'userpeertagging'

    def __str__(self):
        return str(self.communityid+self.aptno)