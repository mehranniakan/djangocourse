from django.db import models


# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=255)
    Subject = models.CharField(max_length=255, null=True)
    Email = models.EmailField()
    Message = models.TextField()
    Created_date = models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    class Meta:
        ordering = ('Created_date',)


class news_letter(models.Model):
    Email = models.EmailField()
    Status = models.BooleanField(default=False)
    Created_date = models.DateTimeField(auto_now_add=True)
    Updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Email

    class Meta:
        ordering = ('Created_date',)
