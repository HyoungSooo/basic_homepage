from django.db import models
from django_resized import ResizedImageField

# Create your models here.
CATEGORY = (
  ("Inter", "Inter"),
  ("Edu", "Edu"),
  ("Res", "Res")
)

POSITION = (
    ('PH_D', 'PH_D'),
    ('Post_Graduate', 'Post_Graduate'),
    ('Undergraduate', 'Undergraduate'),
)

class Professor(models.Model):
    img = models.ImageField(upload_to='prof_img')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    p_num = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fax = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField( max_length=50)
    since = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 

class Timeline(models.Model):

    
    name = models.ForeignKey(Professor, related_name='prof_time', on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices = CATEGORY)
    des = models.CharField(max_length=500)
    start_date = models.DateField( auto_now=False, auto_now_add=False, blank=True, null=True)
    end_date = models.DateField( auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.des

    def __unicode__(self):
        return 

class Member(models.Model):


    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='member_img')
    position = models.CharField(max_length=13, choices=POSITION, blank=False)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    join_date = models.DateField(default='2020-01-01')

    def __str__(self):
        return self.name