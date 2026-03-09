from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.TextField()
    Image=models.ImageField(upload_to='posts/',null=True, blank=True,max_length=255)
    Created_at=models.DateField(auto_now_add=True)

    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Title

