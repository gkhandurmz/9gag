from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField()
    summary = models.TextField(max_length=100)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')
    total_votes = models.IntegerField(default=0)
    SentBy = models.ForeignKey(User, on_delete=models.CASCADE, default=0)


