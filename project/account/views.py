from django.shortcuts import render,redirect, get_object_or_404
from account.forms import signupForm,signinForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from rest_framework.authtoken.models import Token
from .models import Profile, Photos
from django.http import JsonResponse
import json



#==========================SIGN IN===============================

def signin(request):
    if request.method == 'POST':
        form = signinForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])
            if user is not None :
                if user.is_active :
                    login(request,user)
                    token = Token.objects.get(user=user).key
                    return redirect("/")
                else :
                    return render(request,
                                'account/files/signup.html',
                                {'form':form,
                                'response':'Account disabled','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'}) 
            else :
                return render(request,
                                'account/files/signup.html',
                                {'form':form,
                                'response':'Wrong username or password','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'}) 
            
    else:
        form = signinForm()
    return render(request,'account/files/signin.html',{'nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html','form':form})

#========================END SIGN IN=============================




#==========================SIGN UP===============================

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            if User.objects.filter(username = cd['username']).exists():
                return render(request,
                'account/files/signup.html',
                {'form':form,
                'response':'Username Unavailable','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'})
            else:
                if User.objects.filter(email = cd['email']).exists():
                    return render(request,
                    'account/files/signup.html',
                     {'form':form,
                     'response':'Email Already in Use','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'})
                else:
                    if cd['password']==cd['confirm_password']:
                        if len(cd['password']) >= 8:
                            specialCharachter = 0
                            number = 0
                            word = 0
                            for x in cd['password']:
                                if x=='!' or x=='@' or x=='#' or x=='^' or x=='&' or x=='*' or x=='#' or x=='(' or x==')' or x=='-' or x=='_' or x=='=' or x=='+' or x=='{' or x=='}' or x=='[' or x==']' or x=='|' or x=='\\' or x==';' or x==':' or x=='\'' or x=='"' or x=='<' or x=='>' or x==',' or x=='.' or x=='/' or x=='?' :
                                    specialCharachter = specialCharachter + 1
                                if x>='0' and x<='9' :
                                    number = number + 1
                                if (x>='a' and x<='z') or (x>='A' and x<='Z'):
                                    word = word + 1
                            if specialCharachter > 0 and word > 0 and number > 0 :
                                u = User.objects.create_user(first_name=cd['first_name'],email=cd['email'],password=cd['password'],username=cd['username'])
                                Profile.objects.create(user=u)
                                token = Token.objects.get(user=u).key
                                login(request,u)
                                return redirect('/')
                            else:
                                return render(request,
                                'account/files/signup.html',
                                {'form':form,
                                'response':'Password must contain a special charachter (@,!,#....), a number and an alphabet','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'}) 
                        else:
                            return render(request,
                                'account/files/signup.html',
                                {'form':form,
                                'response':'Password too short, must be atleast 8 charachters long','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'})  
                    else:
                        return render(request,
                        'account/files/signup.html',
                        {'form':form,
                        'response':'Password don\'t match','nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html'})
    else:
        form = signupForm()
    return render(request,'account/files/signup.html',{'nav':'common/nav.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html','form':form})

#========================END SIGN UP=============================




#==========================LOG OUT==============================

@login_required
def signout(request):
    logout(request)
    return redirect('/')
#========================END LOG OUT============================




#==========================PROFILE===============================

@login_required
def profile(request):
    photos = Photos.objects.filter(user=request.user)
    return render(request,'account/files/profile.html',{'css':'account/files/profileCss.html','js':'account/files/profileJs.html','commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html','nav':'common/nav.html','photos':photos})   

#========================END PROFILE=============================




#======================RE-AUTHENTICATE============================
@login_required
@require_POST
def re_authenticate(request):
    password = request.POST.get('pass')
    if password!="":
        if request.user.check_password(password) :
            return JsonResponse({'status':'ok'})
        else :
            return JsonResponse({'status':'Wrong Password'})
    else :
        return JsonResponse({'status':'empty'})
    return JsonResponse({'status':'Something Went Wrong'})
#====================END RE-AUTHENTICATE==========================




#========================EDIT PROFILE=============================
@login_required
@require_POST
def editProfile(request):
    firstName = request.POST.get('firstName').strip()
    lastName = request.POST.get('lastName').strip()
    newPassword = request.POST.get('newPassword').strip()
    confirmNewPassword = request.POST.get('confirmNewPassword').strip()
    user = User.objects.get(username = request.user.username)
    if firstName != request.user.first_name and firstName != '' :
        user.first_name = firstName
    if lastName != request.user.last_name and lastName != '' :
        user.last_name = lastName
    if newPassword!='' or confirmNewPassword!='':
        if newPassword==confirmNewPassword:
            if len(newPassword) >= 8:
                specialCharachter = 0
                number = 0
                word = 0
                for x in newPassword:
                    if x=='!' or x=='@' or x=='#' or x=='^' or x=='&' or x=='*' or x=='#' or x=='(' or x==')' or x=='-' or x=='_' or x=='=' or x=='+' or x=='{' or x=='}' or x=='[' or x==']' or x=='|' or x=='\\' or x==';' or x==':' or x=='\'' or x=='"' or x=='<' or x=='>' or x==',' or x=='.' or x=='/' or x=='?' :
                        specialCharachter = specialCharachter + 1
                    if x>='0' and x<='9' :
                        number = number + 1
                    if (x>='a' and x<='z') or (x>='A' and x<='Z'):
                        word = word + 1
                if specialCharachter > 0 and word > 0 and number > 0 :
                    if user.check_password(newPassword):
                        return JsonResponse({'status':'Cannot reuse previous password'})
                    else :
                        user.set_password(newPassword)
                else:
                    return JsonResponse({'status':'Password must contain a special charachter (@,!,#....), a number and an alphabet'})
            else:
                return JsonResponse({'status':'Password too short, must be atleast 8 charachters long'})
        else :
            return JsonResponse({'status':'Passwords don\'t match' })
    user.save()
    return JsonResponse({'status':'ok'})
    #======================END EDIT PROFILE===========================
    

@login_required
@require_POST
def imageUpload(request):
    image = request.FILES.get('image')
    newImage = Photos()
    newImage.user = request.user
    newImage.photo = image
    newImage.save()
    return JsonResponse({'status':'oesrdtk'})