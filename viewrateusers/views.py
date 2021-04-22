from django.shortcuts import render
from .models import Userpreference,Usersdata,UserRating, UserHistory, UserPeerTagging
from community.models import CommunityDetails


def viewrateuser(request):
    return render(request, 'usersearch.html')


def saveuserstatus(request):
    community = request.POST["community"]
    housenumber = request.POST["housenumber"]
    userid = request.user.username
    savepeerdetails(community,housenumber,userid)
    saveuserhistory(userid, community)
    pref = Userpreference.objects.get(userid=userid)
    pref.availablestatus = False
    pref.save(update_fields=['statusavailable'])
    userdetails = Usersdata.objects.get(userid=userid)
    communities = CommunityDetails.objects.all()
    return render(request, 'users/profile.html', {'userdetails':userdetails, 'communities':communities})


def displayuserdetails(request):
    return render(request, 'userdetails.html')


def savepeerdetails(community, housenumber, userid):
    com = CommunityDetails.objects.get(name=community)
    peerrow = UserPeerTagging.objects.filter(communityid=com.communityid, aptno=housenumber)
    print(peerrow[0].userid1)
    if peerrow.exists():
        if peerrow[0].userid1 is None:
            peerrow[0].userid1=userid
            peerrow[0].save(update_fields=['userid1'])
        elif peerrow[0].userid2 is None:
            peerrow[0].userid2 = userid
            peerrow[0].save(update_fields=['userid2'])
        elif peerrow[0].userid3 is None:
            peerrow[0].userid3 = userid
            peerrow[0].save(update_fields=['userid3'])
        elif peerrow[0].userid4 is None:
            peerrow[0].userid4 = userid
            peerrow[0].save(update_fields=['userid4'])
        else: return 'Number of roommates exceeded'
    else:
        UserPeerTagging.objects.create(communityid=com, aptno=housenumber,userid1=userid)
    return


def saveuserhistory(userid,community):
    user = Usersdata.objects.get(userid=userid)
    userhistory = UserHistory.objects.filter(userid=userid)
    if userhistory.exists():
        if userhistory[0].prevapartment1 is None:
            userhistory[0].save(update_fields=['prevapartment1'])
        elif userhistory[0].prevapartment2 is None:
            userhistory[0].save(update_fields=['prevapartment2'])
        elif userhistory[0].prevapartment3 is None:
            userhistory[0].save(update_fields=['prevapartment3'])
        else:
            userhistory[0].save(update_fields=['prevapartment1'])
    else:
        rows = UserHistory.objects.all()
        print(rows)
        UserHistory.objects.create(userid= user, userhistoryid=rows.count()+1, prevapartment1= community)
    return