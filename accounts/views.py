from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .models import DesignProject
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')


def project(request):
    designProject = DesignProject.objects
    if request.method == 'POST':
        JumpTargetLocation = request.POST['Photo']
        print(JumpTargetLocation)
        return render(request, 'accounts/project.html', {'designProject': designProject, 'JumpTargetLocation':JumpTargetLocation})
    else:
        return render(request, 'accounts/project.html', {'designProject': designProject})

def service(request):
    return render(request, 'accounts/service.html')

def contact(request):
    if request.method == 'POST':
        MessageName = request.POST['Message-Name']
        MessageEmail = request.POST['Message-Email']
        MessageCompany = request.POST['Message-Company']
        MessagePhone = request.POST['Message-Phone']
        Message = request.POST['Message']
        MessagePhone ='#Visitor did not provide his/her phone number ' if MessagePhone == '' else MessagePhone
        MessageCompany = '#Visitor did not provide his/her company name' if MessageCompany == '' else MessageCompany
        send_mail(
        '【Message from NTD Website Visitor:'+MessageName + '】',
        Message+'  \n my phone number:'+MessagePhone +'\n my company:'+MessageCompany,
        MessageEmail,#from email
        [' office@ntdeng.net'],#to email
        )

        return render(request, 'accounts/contact.html', {'MessageName': MessageName})
    else:

        return render(request, 'accounts/contact.html',)