from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    return render(request,'register.html')


def reg_data(request):
    user_name = request.POST['txtusername']
    user_email = request.POST['txtemail']
    user_pswd = request.POST['txtpawd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html', {'data': 'Username,email  already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_pswd)
        u1.save()
        return render(request,'home.html',{'data':user_name})


def login(request):
    return render(request,'login.html')


def log_data(request):
    user_name = request.POST['txtusername']
    user_pswd = request.POST['txtpawd']
    user1 = authenticate(username=user_name, password=user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            request.session['name'] = user_name
            return render(request,'home.html',{'data':user_name})
    return render(request,'login.html',{'data':'Username,email not available'})


def admin_reg(request):
    return render(request,'register.html')