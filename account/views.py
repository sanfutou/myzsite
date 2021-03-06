from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
#from .forms import LoginForm
from .forms import  RegistrationForm
#文件存在问题，不能进入127.0.0.1:8000/account/register

def register(request):
    if request.method =="POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return HttpResponse("successfully")
        else:
            return HttpResponse("sorry,your can not register.")
    else:
        user_form = RegistrationForm()
        return render(request, "account/register.html", {"form": user_form})

#            cd =login_form.cleaned_data
#            user =authenticate(username=cd['username'],password=cd['password'])
#
#            if user:
#                login(request,user)
#                return HttpResponse("Wellcome You. You have been authenticated successfully")
#            else:
#                return HttpResponse("Sorry.Your username or password is not right")
#        else:
#            return HttpResponse("Invalid login")
#
#    if request.method == "GET":
#        login_form =LoginForm()
#        return render(request,"account/login.html",{"form":login_form})
