from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class MainMenu(models.Model):
    created_at = models.DateField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=0)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MainMenu, self).save(*args, **kwargs)

class MenuItems(models.Model):
    title = models.CharField(max_length=60, unique=True)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE)
    slug = models.CharField(max_length=60, unique=True)
    status = models.BooleanField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, upload_to='pictures')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    price = models.CharField(max_length=100,default='3')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(MenuItems, self).save(*args, **kwargs)

class Chef(models.Model):
    name = models.CharField(max_length=60, unique=True)
    main_menu = models.ForeignKey(MainMenu, on_delete=models.CASCADE,blank=True)
    description = models.TextField(max_length=400)
    joindate = models.CharField(max_length=60)


class Contactus(models.Model):
    fullname = models.CharField(max_length=60, unique=True)
    email = models.CharField(max_length=60, unique=True)
    subject = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=400)
    date = models.DateTimeField(auto_now_add=True)
