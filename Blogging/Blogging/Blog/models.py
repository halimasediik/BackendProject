from django.db import models

class Articls(models.Model):
    title= models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=50 ,blank=False,null=False)
