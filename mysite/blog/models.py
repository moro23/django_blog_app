from pyexpat import model
import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
 
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_month='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    ##
    objects = models.Manager() ## lets add the default manager
    published = PublishedManager() ## lets add our custom manager

    class Meta:
        ## lets sort the result in descending order 
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    ## lets build a canonical url
    #def get_absolute_url(self):
        #return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id), self.slug])
        #return reverse('blog:post_detail', args=[str(self.slug)])

    