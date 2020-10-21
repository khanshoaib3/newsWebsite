from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


#Custom model manager to filter posts according to published status
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset()\
										   .filter(status='published')


# Create your models here.
class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250,blank=False)
	slug = models.SlugField(max_length=250,unique_for_date='publish',blank=False)
	body = models.TextField(blank=False)
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='newsBlog_post')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	objects = models.Manager() #Django's default model manager/filterer
	published = PublishedManager() #Our custom model manager/filterer
	class Meta:
		ordering = ('-publish',)
	def __str__(self):
		 return self.title