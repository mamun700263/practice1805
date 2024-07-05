from django.shortcuts import render,redirect
from .forms import RegistrationForm,ChangeInformationsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
# Create your views here.

def home(request):
    return render(request,'home.html')


def registration(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account Created Success fully ! please log in ')
            form.save();
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request,'Forms.html',{'form':form,'page':'Registration page'})


@login_required
def profile(request):
    return render(request,'profile.html')


@login_required
def user_logout(request):
    logout(request)
    messages.info(request,'Logged Out Successfully')
    return redirect('login')


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             messages.success(request,'Logged in successfully ')
#             login(request)
#             return redirect('profile')
#     else:
#         form = LoginForm()
#         messages.warning(request,'somthing not ok ')
#     return render(request,'Forms.html',{'form':form,'page':'Log IN Page'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass= form.cleaned_data['password']
            user = authenticate(username = user_name,password = user_pass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged In Successfully')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
            
    return render(request,'Forms.html',{'form':form,'page':'Log in'})
    
    

@login_required
def change_pass_with_old(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            messages.success(request,'Password Changed Successfully ! Please log in again')
            form.save()
            return redirect('profile')
    else:
        form = PasswordChangeForm(request)
    return render(request,'Forms.html',{'form':form,'page':'Password Change'})



@login_required
def change_pass_without_old(request):
    if request.method =='POST':
        form = SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            messages.success(request,'Password Changed Successfully ! Please log in again')
            form.save()
            return redirect('profile')
    else:
        form = SetPasswordForm(request)
    return render(request,'Forms.html',{'form':form,'page':'Password Change'})



@login_required
def change_user_info(request):
    if request.method =='POST':
        form = ChangeInformationsForm(request.POST,instance = request.user)
        # form = ChangeInformationsForm(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request,'Account Information change Success fully !  ')
            form.save();
            return redirect('profile')
    else:
        form = ChangeInformationsForm(instance = request.user)
    return render(request,'Forms.html',{'form':form,'page':'User Information page'})
