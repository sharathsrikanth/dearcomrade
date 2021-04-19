from django.shortcuts import render
from .models import Userpreference,Usersdata,UserRating, UserHistory, UserPeerTagging
from community.models import CommunityDetails


def viewrateuser(request):
    return render(request, 'usersearch.html')


def saveuserstatus(request):
    community = request.POST["community"]
    housenumber = request.POST["housenumber"]
    userid = 'ssrika14'
    savepeerdetails(community,housenumber,userid)
    saveuserhistory(userid, community)
    return


def displayuserdetails(request):
    return render(request, 'userdetails.html')


def savepeerdetails(community, housenumber, userid):
    com = CommunityDetails.objects.get(name=community)
    peerrow = UserPeerTagging.objects.get(communityid=com.communityid, housenumber=housenumber)
    if peerrow:
        if peerrow.userid1 is not None:
            peerrow.userid1=userid
            peerrow.save(update_fields=['userid1'])
        elif peerrow.userid2 is not None:
            peerrow.userid2 = userid
            peerrow.save(update_fields=['userid2'])
        elif peerrow.userid3 is not None:
            peerrow.userid3 = userid
            peerrow.save(update_fields=['userid3'])
        elif peerrow.userid4 is not None:
            peerrow.userid4 = userid
            peerrow.save(update_fields=['userid4'])
        else: return 'Number of roommates exceeded'
    return


def saveuserhistory(community, userid):
    userhistory = UserHistory.objects.get(userid=userid)
    if userhistory:
        if userhistory.prevapartment1 is not None:
            userhistory.save(update_fields=['prevapartment1'])
        elif userhistory.prevapartment2 is not None:
            userhistory.save(update_fields=['prevapartment2'])
        elif userhistory.prevapartment3 is not None:
            userhistory.save(update_fields=['prevapartment3'])
        else:
            userhistory.save(update_fields=['prevapartment3'])
    else:
        UserHistory.objects.create(userid= userid, prevapartment1= community)

    return