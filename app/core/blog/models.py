from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    teaser = models.TextField()
    body = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts",null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title