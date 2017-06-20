# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.shortcuts import render,redirect
from posts.models import Posts,Comments
from django.contrib.auth.decorators import login_required

def posts(request):
    msg = ''
    posts = Posts.objects.all().order_by('-id')
    if request.method == "POST" and request.user.is_authenticated:
        data = request.POST
        if not len(data['content']) > 140:
            Posts(content=data['content'],user_id=request.user).save()
            msg = 'Post criado com sucesso, daqui 1 hora seu post será excluido!'
        else:
            msg = 'Tamanho máximo de caracteres excedido'
    return render(request,'posts.html',{'msg':msg,'posts':posts})

def post(request,post_id):
    msg = ''
    post = Posts.objects.get(id=post_id)
    comments = Comments.objects.filter(post_id=post)
    if request.method == "POST" and request.user.is_authenticated:
        data = request.POST
        if not len(data['content']) > 140:
            Comments(content=data['content'],user_comment=request.user,post_id=post).save()
        else:
            msg = 'Tamanho máximo de caracteres excedido'

    return render(request,'post.html',{'msg':msg,'post':post,'comments':comments})
