# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    content = models.TextField(null=False)
    create_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos',null=True)
    user_id = models.ForeignKey(User,related_name='user_id')

    @property
    def comments(self,):
        return Comments.objects.filter(post_id=self).count()

class Comments(models.Model):
    content = models.TextField(null=False)
    post_id = models.ForeignKey(Posts,related_name='post_id',on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User,related_name='user_comment')
    create_at = models.DateTimeField(auto_now=True)
