from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from user.models import User, Profile
from dcomhomepage.utils import extractImage, extractText, getfilename
from django.conf import settings
from PIL import Image
import io
import os


class PostNotice(models.Model):
    TAGS = (
        ('공지', '공지'),
        ('행사', '행사'),
        ('대회', '대회'),
        ('공모전', '공모전'),
    )

    # blank=True : Form 사용 시 입력 안해도 오류 X
    # null=True : Foreign Key가 null 값을 가져도 되게 함
    title = models.CharField(max_length=50, blank=True, default='')
    content = RichTextUploadingField()
    writerName = models.CharField(max_length=20, blank=True)
    writerStuNo = models.CharField(max_length=3, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    tag = models.CharField(max_length=10, default='공지')
    depth = models.IntegerField(default=0)
    imageLink = models.CharField(max_length=200, default='/static/img/sample/document-icon.png', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return "{} {}: {}".format(self.writerStuNo, self.writerName, self.title)

    def save(self, *args, **kwargs):
        img_link = extractImage(self.content)
        print(img_link)

        if img_link is not None:
            with open(settings.BASE_DIR + img_link, 'rb') as f:
                im = Image.open(io.BytesIO(f.read()))
                size = im.size
                if size[0] > size[1] * 1.25:
                    top = 0
                    bottom = size[1]
                    left = size[0] / 2 - size[1] * 0.625
                    right = size[0] / 2 + size[1] * 0.625
                else:
                    top = size[1] / 2 - size[0] * (1 / 1.25) * 0.5
                    bottom = size[1] / 2 + size[0] * (1 / 1.25) * 0.5
                    left = 0
                    right = size[0]
                croped = im.crop((left, top, right, bottom))
                croped.thumbnail((125, 100))
                link = 'uploads/thumbnail/' + os.path.basename(f.name)
                croped.convert('RGB').save(link, "JPEG", quality=200)
                self.imageLink = '/' + link

        profile = Profile.objects.get(user=self.userIdx)

        if self.parent is not None:
            self.title = 'Comments'
            self.depth = self.parent.depth + 1

        self.writerStuNo = profile.stuNo
        self.writerName = self.userIdx.first_name + self.userIdx.last_name
        self.summary = extractText(self.content)[:200]
        super().save(*args, **kwargs)


class PostActivity(models.Model):
    TAGS = (
        ('행사', '행사'),
        ('대회', '대회'),
        ('프젝', '프젝'),
        ('기타', '기타'),
    )

    # blank=True : Form 사용 시 입력 안해도 오류 X
    # null=True : Foreign Key가 null 값을 가져도 되게 함
    title = models.CharField(max_length=50, blank=True, default='')
    content = RichTextUploadingField()
    writerName = models.CharField(max_length=20, blank=True)
    writerStuNo = models.CharField(max_length=3, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    tag = models.CharField(max_length=10, choices=TAGS, default='공지')
    depth = models.IntegerField(default=0)
    imageLink = models.CharField(max_length=200, default='/static/img/sample/document-icon.png', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return "{} {}: {}".format(self.writerStuNo, self.writerName, self.title)

    def save(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.userIdx)

        if self.parent is not None:
            self.title = 'Comments'
            self.depth = self.parent.depth + 1
        else:
            img_link = extractImage(self.content)

            if img_link is not None:
                with open(settings.BASE_DIR + img_link, 'rb') as f:
                    im = Image.open(io.BytesIO(f.read()))
                    size = im.size
                    if size[0] > size[1] * 1.25:
                        top = 0
                        bottom = size[1]
                        left = size[0] / 2 - size[1] * 0.625
                        right = size[0] / 2 + size[1] * 0.625
                    else:
                        top = size[1] / 2 - size[0] * (1 / 1.25) * 0.5
                        bottom = size[1] / 2 + size[0] * (1 / 1.25) * 0.5
                        left = 0
                        right = size[0]
                    croped = im.crop((left, top, right, bottom))
                    croped = croped.resize((250, 200), Image.ANTIALIAS) ##
                    link = 'uploads/thumbnail/' + os.path.basename(f.name)
                    croped.convert('RGB').save(link, "JPEG", quality=90)
                    self.imageLink = '/' + link

        self.writerStuNo = profile.stuNo
        self.writerName = self.userIdx.first_name + self.userIdx.last_name
        self.summary = extractText(self.content)[:200]
        super().save(*args, **kwargs)


class PostNews(models.Model):
    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writerName = models.CharField(max_length=20, blank=True)
    writerStuNo = models.CharField(max_length=3, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    depth = models.IntegerField(default=0)
    imageLink = models.CharField(max_length=200, default='/static/img/sample/document-icon.png', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)
    tag = models.CharField(max_length=50, default = 'News')

    def __str__(self):
        return "{} {}: {}".format(self.writerStuNo, self.writerName, self.title)

    def save(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.userIdx)

        if self.parent is not None:
            self.title = 'Comments'
            self.depth = self.parent.depth + 1

        img_link = extractImage(self.content)

        if img_link is not None:
            with open(settings.BASE_DIR + img_link, 'rb') as f:
                im = Image.open(io.BytesIO(f.read()))
                size = im.size
                if size[0] > size[1] * 1.25:
                    top = 0
                    bottom = size[1]
                    left = size[0] / 2 - size[1] * 0.625
                    right = size[0] / 2 + size[1] * 0.625
                else:
                    top = size[1] / 2 - size[0] * (1 / 1.25) * 0.5
                    bottom = size[1] / 2 + size[0] * (1 / 1.25) * 0.5
                    left = 0
                    right = size[0]
                croped = im.crop((left, top, right, bottom))
                croped.thumbnail((125, 100))
                link = 'uploads/thumbnail/' + os.path.basename(f.name)
                croped.convert('RGB').save(link, "JPEG", quality=200)
                self.imageLink = '/' + link

        self.writerStuNo = profile.stuNo
        self.writerName = self.userIdx.first_name + self.userIdx.last_name
        self.summary = extractText(self.content)[:200]
        super().save(*args, **kwargs)


class PostOutstanding(models.Model):
    TAGS = (
        ('수상', '수상'),
        ('발표', '발표'),
        ('학회', '학회'),
        ('기타', '기타')
    )

    title = models.CharField(max_length=50, blank=True, default='Comments')
    content = RichTextUploadingField()
    writerName = models.CharField(max_length=20, blank=True)
    writerStuNo = models.CharField(max_length=3, blank=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, blank=True, null=True)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    hit = models.IntegerField(default=0)
    writedAt = models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=50, default='', blank=True)
    tag = models.CharField(max_length=10, choices=TAGS, default='기타')
    depth = models.IntegerField(default=0)
    imageLink = models.CharField(max_length=200, default='/static/img/sample/document-icon.png', blank=True)
    summary = models.CharField(max_length=200, default='', blank=True)

    def __str__(self):
        return "{} {}: {}".format(self.writerStuNo, self.writerName, self.title)

    def save(self, *args, **kwargs):
        img_link = extractImage(self.content)

        if img_link is not None:
            with open(settings.BASE_DIR + img_link, 'rb') as f:
                im = Image.open(io.BytesIO(f.read()))
                size = im.size
                if size[0] > size[1] * 1.25:
                    top = 0
                    bottom = size[1]
                    left = size[0] / 2 - size[1] * 0.625
                    right = size[0] / 2 + size[1] * 0.625
                else:
                    top = size[1] / 2 - size[0] * (1 / 1.25) * 0.5
                    bottom = size[1] / 2 + size[0] * (1 / 1.25) * 0.5
                    left = 0
                    right = size[0]
                croped = im.crop((left, top, right, bottom))
                croped.thumbnail((125, 100))
                link = 'uploads/thumbnail/' + os.path.basename(f.name)
                croped.convert('RGB').save(link, "JPEG", quality=200)
                self.imageLink = '/' + link

        profile = Profile.objects.get(user=self.userIdx)

        if self.parent is not None:
            self.title = 'Comments'
            self.depth = self.parent.depth + 1

        self.writerStuNo = profile.stuNo
        self.writerName = self.userIdx.first_name + self.userIdx.last_name
        self.summary = extractText(self.content)[:200]
        super().save(*args, **kwargs)


class PostOutstandingMember(models.Model):
    studyIdx = models.ForeignKey(PostOutstanding, on_delete=models.CASCADE)
    userIdx = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.name = self.userIdx.first_name + self.userIdx.last_name
        super().save(*args, **kwargs)

