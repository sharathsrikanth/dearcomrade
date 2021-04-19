from django.shortcuts import render


def home(request):
    return render(request, 'dearcomradehome/home.html')


def about(request):
    print(request.user.username)
    return render(request, 'dearcomradehome/about.html', {'title': 'About'})