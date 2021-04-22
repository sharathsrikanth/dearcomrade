from django.shortcuts import render
from .models import Userpreference,Usersdata,UserRating,ResultantTempUserTable
from django.db.models import Q


def findroommate(request):
    preferences = Userpreference.objects.all()
    return render(request, 'findroommate.html', {'preferences': preferences})


def displaypotentialroommatelist(request):
    ResultantTempUserTable.objects.all().delete()
    userdetails = Usersdata.objects.get(userid='ssrika14')

    preference = Userpreference.objects.get(userid='ssrika14')
    sex = userdetails.sex
    users = Userpreference.objects.filter(~Q(userid='ssrika14'),preflocation=preference.preflocation, prefsex=sex, usersex=preference.prefsex,
                                          budget__gte=(preference.budget-100), budget__lte=(preference.budget+100),
                                          cleanliness__gte=(preference.cleanliness-0.5), cleanliness__lte=(preference.cleanliness+0.5))[:30]
    getorderedcompatibleusers(users)
    count = ResultantTempUserTable.objects.all().count()
    if count < 20:
        users = Userpreference.objects.filter(~Q(userid='ssrika14'), preflocation=preference.preflocation, prefsex=sex,
                                              usersex=sex)[:20-count]
    getorderedcompatibleusers(users)
    count = ResultantTempUserTable.objects.all().count()

    if count < 20:
        users = Userpreference.objects.filter(~Q(userid='ssrika14'), preflocation=preference.preflocation)[:20 - count]
    userstodisplay = ResultantTempUserTable.objects.order_by('avgrating')

    #scorecompatibility logic goes here

    return render(request, 'displaylist.html', {'users': userstodisplay})


def displayroommate(request):
    return


def findroommates(request):
    return


def getorderedcompatibleusers(users):
    for user in users:
        temp = UserRating.objects.get(userid=user.userid)
        tempuser = Usersdata.objects.get(userid=user.userid)
        name = tempuser.fname+tempuser.lname
        age = tempuser.age
        avguserrating = getavgrating(temp)
        profilepicture = tempuser.profilepicurl
        ResultantTempUserTable.objects.create(userid=user.userid, name=name, age=age, avgrating=avguserrating, compatibilityscore=0.5, profilepicurl=profilepicture)
    return


def getavgrating(userating):
    avgrating = 0
    if userating.peerrating > 0:
        avgrating += userating.peerrating
    if userating.guestrating > 0:
        avgrating += userating.guestrating
    if userating.communityrating > 0:
        avgrating += userating.communityrating

    if avgrating > 0:
        avgrating = avgrating/3

    return avgrating