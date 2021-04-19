from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from viewrateusers.models import Usersdata,Userpreference,UserRating,UserComments


class ResultantTempUserTable (models.Model):
    userid = models.ForeignKey(Usersdata, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    avgrating = models.IntegerField()
    compatibilityscore = models.FloatField(validators=[MaxValueValidator(1), MinValueValidator(0)])
    profilepicurl = models.CharField(max_length=2083)

    class Meta:
        db_table = 'resultanttempusertable'

    def __str__(self):
        return str(self.userid)