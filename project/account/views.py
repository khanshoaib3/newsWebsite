from django.shortcuts import render,redirect
from account.forms import signupForm,signinForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from .models import Profile


# region Log IN

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

# endregion

# region Sign UP

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

# endregion

# region Log OUT

@login_required
def signout(request):
    logout(request)
    return redirect('/')

# endregion

# region Profile

@login_required
def profile(request):
    return render(request,'account/files/profile.html',{'commonCss':'account/files/commonCss.html','commonJs':'account/files/commonJs.html','nav':'common/nav.html'})   

# endregion
