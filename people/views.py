from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required # required for the user to see the page
def profile_listing(request):
    data = {
        'profiles' : User.objects.filter(is_staff=False)
    }
    return render(request, 'profile_listing.html', data)

@login_required
def profile(request, profile_id):
    if request.user.is_authenticated and request.user.is_staff:
        profile = get_object_or_404(User, id=profile_id)
    else:
        profile = get_object_or_404(User, id=profile_id, is_staff=False)

    data = {
        'profile' : profile,
    }

    return render(request, 'profile.html', data)
