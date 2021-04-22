from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from viewrateusers.models import Usersdata
from community.models import CommunityDetails


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please enter your preferences to get started')
            return render(request, 'users/userregistration.html',{'userid':username})
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def completeuserregistration(request):
    rows = Usersdata.objects.all()
    userid = request.POST.get('userid')
    print(request.POST.get('userid'))
    print('inside')
    Usersdata.objects.create(userid=userid,fname=request.POST["firstname"], lname=request.POST["lastname"], phnumber=request.POST["phonenumber"], age=request.POST["age"],
                             sex=request.POST["sex"], addr1=request.POST["addr1"], addr2=request.POST["addr2"], country=request.POST["country"],
                             description=request.POST["description"], workinfo=request.POST["workinfo"])
    return redirect('login')


@login_required
def profile(request):
    username = request.user.username
    userdetails = Usersdata.objects.get(userid='ssrika14')
    communities = CommunityDetails.objects.all()
    return render(request, 'users/profile.html', {'userdetails':userdetails, 'communities':communities})
