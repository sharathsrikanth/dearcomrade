from django.shortcuts import render
from .models import CommunityDetails


def findcommunities(request):
    communities = CommunityDetails.objects.all()
    return render(request, 'displaycommunities.html', {'communities': communities})


def displaycommunity(request):
    id = request.POST.get('communityid')
    community = CommunityDetails.objects.get(communityid=id)
    return render(request, 'displaycommunity.html', {'community': community})