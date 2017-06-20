from __future__ import unicode_literals
from posts.models import Posts
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger
from django.utils import timezone
from datetime import timedelta

@periodic_task(run_every=(crontab(minute='*/1')),name="delete_posts",ignore_result=False)
def excludePosts():
    time_threshold =  timezone.now() - timedelta(minutes=30)
    posts = Posts.objects.filter(create_at__lte=time_threshold)
    print posts
    posts.delete()
