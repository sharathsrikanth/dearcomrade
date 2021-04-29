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
    ResultantTempUserTable.objects.all().delete()
    userdetails = Usersdata.objects.get(userid=request.user.username)
    sex = userdetails.sex

    preference = Userpreference.objects.get(userid=request.user.username)
    if request.POST.get('city'):
        current_city_pref = request.POST.get('city')
    else:
        current_city_pref=preference.preflocation

    if request.POST.get('budget'):
        current_budget_pref = request.POST.get('budget')
    else:
        current_budget_pref=preference.budget
    if request.POST.get('sex'):
        current_sex_pref = request.POST.get('sex')
    else:
        current_sex_pref=preference.prefsex

    if preference.statusavailable:
        users = Userpreference.objects.filter(~Q(userid=request.user.username),preflocation=current_city_pref, prefsex=current_sex_pref, usersex=preference.prefsex,
                                              budget__gte=(current_budget_pref-100), budget__lte=(current_budget_pref+100),
                                              cleanliness__gte=(preference.cleanliness-0.5), cleanliness__lte=(preference.cleanliness+0.5))[:30]
        if users.exists():
            getorderedcompatibleusers(users)
        count = ResultantTempUserTable.objects.all().count()

        if count < 20:
            users = Userpreference.objects.filter(~Q(userid=request.user.username), preflocation=current_city_pref, prefsex=sex,
                                                  usersex=current_sex_pref)[:20-count]
        if users.exists():
            getorderedcompatibleusers(users)

        count = ResultantTempUserTable.objects.all().count()

        if count < 20:
            users = Userpreference.objects.filter(~Q(userid=request.user.username), preflocation=current_sex_pref)[:20 - count]

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
    for usertocalculate in users:
        print(usertocalculate.userid)
        temp = UserRating.objects.filter(userid=usertocalculate.userid)
        tempuser = Usersdata.objects.get(userid=usertocalculate.userid)
        name = tempuser.fname+tempuser.lname
        age = tempuser.age
        print(temp)
        profilepicture = tempuser.profilepicurl
        if temp:
            avguserrating = getavgrating(temp[0])
            userexists = ResultantTempUserTable.objects.filter(userid=usertocalculate.userid)
            if not userexists.exists():
                ResultantTempUserTable.objects.create(userid=usertocalculate.userid, name=name, age=age, avgrating=avguserrating,
                                                     profilepicurl=profilepicture)
        else:
            userexists = ResultantTempUserTable.objects.filter(userid=usertocalculate.userid)
            if not userexists.exists():
                ResultantTempUserTable.objects.create(userid=usertocalculate.userid, name=name, age=age,
                                                       profilepicurl=profilepicture)
    return


def getavgrating(userating):
    avgrating = 0
    if userating.peerrating:
        avgrating += userating.peerrating
    if userating.guestrating:
        avgrating += userating.guestrating
    if userating.communityrating:
        avgrating += userating.communityrating

    if avgrating > 0:
        avgrating = avgrating/3

    return avgrating