from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import uuid


#Custom model manager to filter posts according to published status
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset()\
										   .filter(status='published')


# Create your models here.
class Post(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	title = models.CharField(max_length=250,blank=False)
	slug = models.SlugField(max_length=250,unique_for_date='publish',blank=False)
	body = models.TextField(blank=False)
	thumbnail = models.CharField(max_length=50,blank=True,default='WLUHO9A_xik',help_text='ONLY UNSPLASH IMAGE_IDS')
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
	def get_absolute_url(self):
		 return reverse('newsBlog:detail',args=[self.publish.year,
		 										self.publish.month,
												self.publish.day, self.slug])