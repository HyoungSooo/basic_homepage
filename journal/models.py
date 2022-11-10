from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

SELECTOR = (
  ("International", "International"),
  ("Domestic", "Domestic"),
)

class Year(models.Model):
  year = models.CharField(max_length=50)

  def __str__(self):
    return self.year

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Year'
    verbose_name_plural = 'Years'


class Papers(models.Model):

    ordering = models.IntegerField(blank=True, null=True)

    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name ="Ypaper")
    title = models.CharField(max_length = 500)
    category = models.CharField(max_length = 100, choices = SELECTOR)

    def __str__(self):
        return self.title

class Patents(models.Model):

    ordering = models.IntegerField(blank=True, null=True)

    year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name ="Ypatent")
    title = models.CharField(max_length = 500)

    def __str__(self):
        return self.title

class Conferences(models.Model):
  ordering = models.IntegerField(blank=True, null=True)

  year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name ="Yconfer")
  title = models.CharField(max_length = 500)
  category = models.CharField(max_length = 100, choices = SELECTOR)

  def __str__(self):
    return self.title

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Conferences'
    verbose_name_plural = 'Conferencess'

SELECTOR_PROJECT = (
  ("Active", "Active"),
  ("Finish","Finish"),
)

class Projects(models.Model):
  ordering = models.IntegerField(blank=True, null=True)
  year = models.ForeignKey(Year, on_delete=models.CASCADE, related_name ="Yproject")
  title = models.CharField(max_length = 500)
  category = models.CharField(max_length = 100, choices = SELECTOR_PROJECT)
  start_date = models.DateField(auto_now=False, auto_now_add=False)
  end_date = models.DateField(auto_now=False, auto_now_add=False , blank=True, null=True)

  def __str__(self):
    return self.title

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'Projects'
    verbose_name_plural = 'Projectss'

class Research(models.Model):
    img = models.ImageField(upload_to="research")
    one_word_title = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    des = models.CharField(max_length=200)
    detail = RichTextUploadingField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("research")
