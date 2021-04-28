from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from viewrateusers.models import Usersdata
from community.models import CommunityDetails,CommunityUserDetails


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            type = request.POST.get('registrationtype').lower()
            form.save()
            username = form.cleaned_data.get('username')
            if type == 'user':
                messages.success(request, f'Your account has been created! Please enter your data to get started')
                return render(request, 'users/userregistration.html',{'userid':username})
            elif type == 'community':
                messages.success(request, f'Your account has been created! Please enter your community to get continue')
                communities = CommunityDetails.objects.all()
                return render(request, 'users/communityregistration.html', {'communityuserid': username, 'communities':communities})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def completeuserregistration(request):
    if request.POST:
        rows = Usersdata.objects.all()
        userid = request.POST.get('userid')
        print(request.POST.get('userid'))
        Usersdata.objects.create(userid=userid,fname=request.POST["firstname"], lname=request.POST["lastname"], phnumber=request.POST["phonenumber"], age=request.POST["age"],
                                 sex=request.POST["sex"].lower(), addr1=request.POST["addr1"], addr2=request.POST["addr2"], country=request.POST["country"],
                                 description=request.POST["description"], workinfo=request.POST["workinfo"])
        return redirect('login')
    else:
        messages.error(request, f'Could receive the data, Try again!')
        return redirect('login')

def completecommunityuserregistration(request):
    if request.POST:
        communityuserid = request.POST.get('communityuserid')
        community = CommunityDetails.objects.get(name=request.POST.get('community'))
        id = community.communityid
        CommunityUserDetails.objects.create(communityid=community, name=community.name, communityuserid=communityuserid)
        return redirect('login')
    else:
        messages.error(request, f'Could receive the community details and account created with default community')
        return redirect('login')

@login_required
def profile(request):
    communities = CommunityDetails.objects.all()
    usertoken = CommunityUserDetails.objects.filter(communityuserid=request.user.username)
    print(usertoken)
    if usertoken.exists():
        return render(request, 'users/profile.html', {'userdetails':usertoken,'communities':communities, 'usertoken': usertoken})
    else:
        userdetails = Usersdata.objects.get(userid=request.user.username)
        return render(request, 'users/profile.html', {'userdetails':userdetails,'communities':communities, 'usertoken': False})

