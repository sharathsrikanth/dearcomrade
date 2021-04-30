from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from viewrateusers.models import Usersdata,Userpreference,UserRating,UserComments,UserHistory


class ResultantTempUserTable (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    age = models.IntegerField(null=True)
    avgrating = models.IntegerField(null=True)
    compatibilityscore = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)], null=True)
    profilepicurl = models.CharField(max_length=2083,null=True)

    class Meta:
        db_table = 'resultanttempusertable'

    def __str__(self):
        return str(self.userid)