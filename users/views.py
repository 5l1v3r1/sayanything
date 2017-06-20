# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import timedelta


def checkUser(username):
    try:
        User.objects.get(username=username)
        return True
    except:
        return False

def dashboard(request):
    if request.user.is_authenticated:
        return redirect('posts')
    return render(request,'index.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('posts')
    msg = None
    if request.method == 'POST':
        data = request.POST
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is not None:
            login(request,user)
            return redirect('posts')
        else:
            msg = 'Dados de acesso inválidos'
    return render(request,'login.html',{"error":msg})

def userRegister(request):
    if request.user.is_authenticated:
        return redirect('posts')
    msg = ''
    username = request.GET.get('username','')
    if request.method == 'POST':
        data = request.POST
        if not checkUser(data['username']):
            if data['password'] == data['password_conf']:
                user = User.objects.create_user(username=data['username'],
                password=data['password'])
                return redirect('dashboard')
            else:
                msg = 'Confira suas senhas'
        else:
            msg = 'Usuario já existe'
    return render(request,'register.html',{'username':username,"error":msg})

@login_required(login_url='userLogin')
def userLogout(request):
    logout(request)
    return redirect('dashboard')
