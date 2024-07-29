
from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.db import models
from django_summernote.fields import SummernoteTextField
from taggit.managers import TaggableManager
from django_quill.fields import QuillField


class Category(models.Model):
    Name = models.CharField(max_length=255)

    def __str__(self):
        return self.Name


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    Author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Title = models.CharField(max_length=255)
    Content = QuillField()
    Image = models.ImageField(upload_to='Blog/Images', default='default.jpg')
    Category = models.ManyToManyField(Category)
    Tags = TaggableManager()
    Counted_Views = models.IntegerField(default=0)
    Status = models.BooleanField(default=True)
    Publish_date = models.DateTimeField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Email = models.EmailField()
    Subject = models.CharField(max_length=255)
    Message = models.TextField()
    Approved = models.BooleanField(default=False)
    Created_Date = models.DateTimeField(auto_now_add=True)
    Updated_Date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Subject
