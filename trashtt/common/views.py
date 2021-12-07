from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from common.models import Profile
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.greenpoint = 0
    user.profile.coupon = 0
    user.save()

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile = Profile.objects.get(user = request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'pybo/mypage.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required(login_url='common:login')
def change(request):
    """
    정보변경
    """
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user = user_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('pybo:mypage')
        else:
            update_session_auth_hash(request, user_form)
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'common/change.html', {'user_form': user_form})
