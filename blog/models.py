# https://docs.djangoproject.com/en/5.0/topics/db/models/

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

options = (
    ('draft','Draft'),
    ('published', 'Published'),
)

class Category(models.Model):
    # no need of declaring id
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Post(models.Model):

    #filter by published posts
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'published')

    category = models.ForeignKey(
        Category, on_delete = models.PROTECT, default =1)
    title = models.CharField(max_length =250)
    excerpt = models.TextField(null = True)
    content = models.TextField()
    slug = models.SlugField(max_length = 250, unique_for_date ='published')
    published = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name = 'blog_posts')
    status = models.CharField(max_length=10,choices = options, default = 'published' )
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
    
