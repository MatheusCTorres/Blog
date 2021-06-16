from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) # url text from post link ex: www.test.com/blog/initial-introduction
    author = models.ForeignKey(User, on_delete=models.CASCADE) # reference from id user
    body = models.TextField()  # body from post
    created = models.DateTimeField(auto_now_add=True)  # will add automatically date and hour when we create a post
    updated = models.DateTimeField(auto_now=True)  # every modification will refresh the date 


    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:details", kwargs={"slug": self.slug})


# CRUD for posts
