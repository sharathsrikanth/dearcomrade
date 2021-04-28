from django.shortcuts import render
from .models import Userpreference, Usersdata, UserRating, UserHistory, UserPeerTagging, UserComments
from community.models import CommunityDetails, CommunityUserDetails


def viewrateuser(request):
    return render(request, 'usersearch.html')


def saveuserstatus(request):
    if request.POST:
        community = request.POST["community"]
        housenumber = request.POST["housenumber"]
        userid = request.user.username
        pref = Userpreference.objects.get(userid=userid)
        message = None
        if pref.statusavailable is True:
            message = savepeerdetails(community,housenumber,userid)
            saveuserhistory(userid, community)
            pref.statusavailable = False
            pref.save(update_fields=['statusavailable'])
        else:
            pref.statusavailable = True
            pref.save(update_fields=['statusavailable'])
            message = 'Status changed successfully!'
        userdetails = Usersdata.objects.get(userid=userid)
        communities = CommunityDetails.objects.all()
        return render(request, 'users/profile.html', {'userdetails':userdetails, 'communities':communities,'message':message, 'usertoken': False    }, )
    else:
        userdetails = Usersdata.objects.get(userid=request.user.username)
        communities = CommunityDetails.objects.all()
        return render(request, 'users/profile.html', {'userdetails': userdetails, 'communities': communities, 'usertoken': False})


def displayuserdetails(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    users = Usersdata.objects.filter(fname__contains=fname, lname__contains=lname)
    if users.exists():
        return render(request, 'userdetails.html', {'users':users})
    else:
        return render(request, 'userdetails.html', {'message': 'No Users Found! Please search for a different customer'})


def searchusers(request):
    selecteduser = Usersdata.objects.get(userid=request.POST["userid"])
    print(selecteduser.fname)
    comments = UserComments.objects.filter(userid=request.POST["userid"])[:5]
    ratings = UserRating.objects.get(userid=request.POST["userid"])
    return render(request, 'usersdisplay.html', {'usersdetails': selecteduser, 'usercomments': comments, 'userratings': ratings})


def savepeerdetails(community, housenumber, userid):
    com = CommunityDetails.objects.get(name=community)
    peerrow = UserPeerTagging.objects.filter(communityid=com.communityid, aptno=housenumber)
    peerrowupdate = UserPeerTagging.objects.get(communityid=com.communityid, aptno=housenumber)
    if peerrow.exists():
        if peerrowupdate.userid1 != userid and peerrowupdate.userid2 != userid and peerrowupdate.userid3 != userid and peerrowupdate.userid4 != userid:
            if not peerrow[0].userid1:
                peerrowupdate.userid1=userid
                peerrowupdate.save(update_fields=['userid1'])
            elif not peerrow[0].userid2:
                peerrowupdate.userid2=userid
                peerrowupdate.save(update_fields=['userid2'])
            elif not peerrow[0].userid3:
                peerrowupdate.userid3 = userid
                peerrowupdate.save(update_fields=['userid3'])
            elif not peerrow[0].userid4:
                peerrowupdate.userid4 = userid
                peerrowupdate.save(update_fields=['userid4'])
            else: return 'Number of roommates exceeded'
    else:
        UserPeerTagging.objects.create(communityid=com, aptno=housenumber,userid1=userid)
    return 'Success'


def saveuserhistory(userid,community):
    user = Usersdata.objects.get(userid=userid)
    userhistory = UserHistory.objects.filter(userid=userid)
    userhistoryupdate = UserHistory.objects.get(userid=userid)
    if userhistory.exists():
        if not userhistory[0].prevapartment1:
            userhistoryupdate.save(update_fields=['prevapartment1'])
        elif not userhistory[0].prevapartment2:
            userhistoryupdate.save(update_fields=['prevapartment2'])
        elif not userhistory[0].prevapartment3:
            userhistoryupdate.save(update_fields=['prevapartment3'])
        else:
            userhistoryupdate.save(update_fields=['prevapartment1'])
    else:
        rows = UserHistory.objects.all()
        UserHistory.objects.create(userid= user, userhistoryid=rows.count()+1, prevapartment1= community)
    return


def addcommentratings(request):
    comment = request.POST.get('comment')
    rating = request.POST.get('rating')
    userid = request.POST.get('userid')
    loggedinuser = request.user.username
    user = Usersdata.objects.get(userid=userid)
    communityuserqueryset = CommunityUserDetails.objects.filter(communityuserid=loggedinuser)
    currentuserrating = UserRating.objects.get(userid=userid)
    print('rating')
    print(rating)
    print(currentuserrating)

    if comment:
        rows = UserComments.objects.all()
        UserComments.objects.create(userid=user, commentid=rows.count()+1, comment=comment)

    if rating:
        currentusercheck = UserPeerTagging.objects.filter (userid1=loggedinuser) | UserPeerTagging.objects.filter (userid2=loggedinuser) |UserPeerTagging.objects.filter(userid3=loggedinuser) |UserPeerTagging.objects.filter (userid4=loggedinuser)

        selectedusercheck = UserPeerTagging.objects.filter(userid1=userid) | UserPeerTagging.objects.filter(
            userid2=userid) | UserPeerTagging.objects.filter(
            userid3=userid) | UserPeerTagging.objects.filter(userid4=userid)

        if currentusercheck[0].communityid == selectedusercheck[0].communityid and currentusercheck[0].aptno == selectedusercheck[0].aptno:
            if currentuserrating:
                if currentuserrating.peerrating:
                    currentrating = currentuserrating.peerrating+float(rating)
                    currentrating = currentrating/2
                else:
                    currentrating = float(rating)
                currentuserrating.peerrating = currentrating
                currentuserrating.save(update_fields=['peerrating'])
            else:
                rowcount=UserRating.objects.all()
                currentrating = float(rating)
                UserRating.objects.create(userid=user, ratingid=rowcount.count()+1,peerrating=currentrating)

        elif communityuserqueryset.exists():
            comuser=CommunityUserDetails.objects.get(communityuserid=loggedinuser)
            if loggedinuser == comuser:
                if currentuserrating:
                    if currentuserrating.communityrating:
                        currentrating = currentuserrating.communityrating+float(rating)
                        currentrating = currentrating / 2
                    else:
                        currentrating = float(rating)

                    currentuserrating.communityrating = currentrating
                    currentuserrating.save(update_fields=['peerrating'])
                else:
                    rowcount=UserRating.objects.all()
                    if currentuserrating.communityrating:
                        currentrating = currentuserrating.peerrating + float(rating)
                        currentrating = currentrating / 2
                    else:
                        currentrating = float(rating)
                    UserRating.objects.create(userid=user, ratingid=rowcount.count()+1,peerrating=currentrating)
        else:
            if currentuserrating:
                if currentuserrating.guestrating:
                    currentrating = currentuserrating.guestrating+float(rating)
                    currentrating = currentrating / 2
                else:
                    currentrating = float(rating)

                currentuserrating.guestrating = currentrating
                currentuserrating.save(update_fields=['guestrating'])
            else:
                rowcount=UserRating.objects.all()
                currentrating = rating
                UserRating.objects.create(userid=user, ratingid=rowcount.count()+1,guest=currentrating)

    return render(request, 'usersearch.html')


