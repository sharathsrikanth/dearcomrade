from django.shortcuts import render
from .models import Userpreference,Usersdata,UserRating,ResultantTempUserTable
from community.models import CommunityUserDetails
from django.db.models import Q
from . import fuzzyscore


def findroommate(request):
    usertoken = CommunityUserDetails.objects.filter(communityuserid=request.user.username)
    if usertoken.exists():
        return render(request, 'findroommate.html', {'preferences': None, 'usertoken': usertoken})
    else:
        preferences = Userpreference.objects.get(userid=request.user.username)
        return render(request, 'findroommate.html', {'preferences': preferences, 'usertoken': False})


def displaypotentialroommatelist(request):
    current_city_pref = request.POST.get('city')
    current_budget = request.POST.get('budget')
    current_sex_pref = request.POST.get('sex')


    ResultantTempUserTable.objects.all().delete()
    userdetails = Usersdata.objects.get(userid=request.user.username)
    sex = userdetails.sex
    preference = Userpreference.objects.get(userid=request.user.username)

    if preference.statusavailable:
        users = Userpreference.objects.filter(~Q(userid=request.user.username),preflocation=preference.preflocation, prefsex=sex, usersex=preference.prefsex,
                                              budget__gte=(preference.budget-100), budget__lte=(preference.budget+100),
                                              cleanliness__gte=(preference.cleanliness-0.5), cleanliness__lte=(preference.cleanliness+0.5))[:30]
        if users.exists():
            getorderedcompatibleusers(users)
        count = ResultantTempUserTable.objects.all().count()
        if count < 20:
            users = Userpreference.objects.filter(~Q(userid=request.user.username), preflocation=preference.preflocation, prefsex=sex,
                                                  usersex=sex)[:20-count]
        if users.exists():
            getorderedcompatibleusers(users)
        count = ResultantTempUserTable.objects.all().count()

        if count < 20:
            users = Userpreference.objects.filter(~Q(userid=request.user.username), preflocation=preference.preflocation)[:20 - count]

        if users.exists():
            getorderedcompatibleusers(users)
        userstodisplay = ResultantTempUserTable.objects.all()

        #scorecompatibility logic goes here
        fuzzyscore.findscores(userstodisplay, preference)
        userstodisplayfinal = ResultantTempUserTable.objects.distinct().order_by('avgrating')

        if userstodisplayfinal:
            return render(request, 'displaylist.html', {'users': userstodisplayfinal})
        else:
            return render(request, 'displaylist.html', {'users': 'No users to display'})


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
        profilepicture = tempuser.profilepicurl
        if temp:
            avguserrating = getavgrating(temp)
            userexists = ResultantTempUserTable.objects.filter(userid=user.userid)
            if not userexists.exists():
                ResultantTempUserTable.objects.create(userid=user.userid, name=name, age=age, avgrating=avguserrating,
                                                     profilepicurl=profilepicture)
        else:
            userexists = ResultantTempUserTable.objects.filter(userid=user.userid)
            if not userexists.exists():
                ResultantTempUserTable.objects.create(userid=user.userid, name=name, age=age,
                                                       profilepicurl=profilepicture)
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