from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth
from .models import User_profile
from django.contrib.auth.decorators import login_required

# Create your views here.

User = get_user_model()

def sign_up_start(request):

    return render(request, 'accounts/sign_up_start.html')

def sign_up(request):
    context = {}
    
    #POST Method
    if request.method == 'POST':
        if (request.POST['email'] and
                request.POST['password'] and
                request.POST['password'] == request.POST['password_check']):

            new_user = User.objects.create_user(
                email=request.POST['email'],
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                gender=request.POST['gender'],
                password=request.POST['password'],
            )

            auth.login(request, new_user)
            # profile = User_profile(user=request.user)
            # profile.save()
            # user= new_user
            # user_id=new_user.id
            return redirect('accounts:sign_up_profile')
    
        else:
            context['error'] = 'Password를 확인해주세요'
    #GET Method    
    return render(request, 'accounts/sign_up.html', context)

def sign_up_profile(request):

    context = {}

    user = request.user  

    #POST Method
    if request.method == 'POST':
        if (request.POST['main_viliage'] ):

            main_viliage = request.POST['main_viliage']
            # profile = User_profile(user=user, introduce=introduce, main_viliage=main_viliage)
            profiles = User_profile(main_viliage=main_viliage)
            profiles.save()

            if (request.POST['second_viliage'] and
                    request.POST['third_viliage'] ):
                    
                user = request.user
                profiles.second_viliage = request.POST['second_viliage']
                profiles.third_viliage = request.POST['third_viliage']
                # profile = User_profile(user=user, second_viliage=second_viliage, third_viliage=third_viliage)
                profiles.save()
            
            return redirect('posts:profile_page', user_id=user.id)
    
        else:
            context['error'] = '자기소개와 우리 동네는 꼭 입력해주세요.'
            
    #GET Method    
    return render(request, 'accounts/sign_up_profile.html', context)




def login(request):
    context ={}
    
    #POST Method
    
    if request.method == 'POST':
        if request.POST['email'] and request.POST['password']:
            
            user = auth.authenticate(
                request,
                email=request.POST['email'],
                password=request.POST['password']
            )
            
            if user is not None:
                auth.login(request, user)
                return redirect('posts:index')
            else:
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
            
        else:
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'
            
    # GET Method
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('posts:index')

@login_required
def new_profile(request, user_id):

    # user_id=request.user.id    
    
    return redirect('accounts:update_profile', user_id=request.user.id)

@login_required
def update_profile(request, user_id):

    context = {}

    user = request.user
    profiles = User_profile.objects.get(user_id=user.id)
  

    #POST Method
    if request.method == 'POST':
        if (request.POST['introduce'] and
                request.POST['main_viliage'] ):

            profiles.introduce = request.POST['introduce']
            profiles.main_viliage = request.POST['main_viliage']
            # profile = User_profile(user=user, introduce=introduce, main_viliage=main_viliage)
            profiles.save()

            if (request.POST['second_viliage'] and
                    request.POST['third_viliage'] ):
                    
                user = request.user
                profiles.second_viliage = request.POST['second_viliage']
                profiles.third_viliage = request.POST['third_viliage']
                # profile = User_profile(user=user, second_viliage=second_viliage, third_viliage=third_viliage)
                profiles.save()
            
            return redirect('posts:profile_page', user_id=user.id)
    
        else:
            context['error'] = '자기소개와 우리 동네는 꼭 입력해주세요.'
            
    context['profiles'] = profiles
    #GET Method    
    return render(request, 'accounts/update_profile.html', context)