from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True,null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True) 
    def __str__(self):
      return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
      
        super(Post, self).save(*args, **kwargs)