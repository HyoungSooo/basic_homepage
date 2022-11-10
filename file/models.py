from django.db import models
from board.models import Board
from post.models import PostNotice, PostActivity, PostNews,PostOutstanding
import time


def make_filename(instance, filename):
    return str(time.time()) + '_' + filename


# File Field 참고 URL : https://cjh5414.github.io/django-file-upload/
class FileNotice(models.Model):
    token = models.CharField(max_length=200)
    post = models.ForeignKey(PostNotice, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to=make_filename)


class FileActivity(models.Model):
    token = models.CharField(max_length=200)
    post = models.ForeignKey(PostActivity, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to=make_filename)


class FileFree(models.Model):
    token = models.CharField(max_length=200)
    post = models.ForeignKey(PostNews, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to=make_filename)

class FileStudy(models.Model):
    token = models.CharField(max_length=200)
    post = models.ForeignKey(PostOutstanding, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to=make_filename)
