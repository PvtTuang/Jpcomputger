from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from accounts.models import *
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def user_is_owner(user):
    return user.is_authenticated and user.profile.role.name == 'Owner'

def loginpage(request):
    return render(request,"accounts/loginpage.html")


def line_login_callback(request):
    return HttpResponse("You've successfully logged in with LINE!")

@login_required
@user_passes_test(user_is_owner, login_url='/')
def show_user(request):
    profiles = Profile.objects.select_related('user', 'role').all()
    return render(request, 'accounts/user.html', {'profiles': profiles})

@login_required
def profile(request):
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
@user_passes_test(user_is_owner, login_url='/')
def block_user(request, user_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, user_id=user_id)
        
        if profile.role.name == Role.OWNER:
            return redirect('user')
        
        if profile.role.name == Role.BLOCKED:
            profile.role = Role.objects.get(name=Role.CUSTOMER)
        else:
            profile.role = Role.objects.get(name=Role.BLOCKED)
        
        profile.save()
        return redirect('user')
    
    return redirect('user')

