from django import forms
from django.contrib.auth.models import User

class signinForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))

class signupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}))

class reAuthenticate(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'innerInput','onmouseover':'inputHover(this)','onmouseout':'inputHover(this)','onchange':'inputChange(this)'}),label="")
