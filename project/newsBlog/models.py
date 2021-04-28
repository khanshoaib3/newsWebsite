from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.translation import ugettext_lazy as _
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
import uuid


#Custom model manager to filter posts according to published status
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset()\
										   .filter(status='published')

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


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
	thumbnail = models.CharField(max_length=50,blank=True,default='WLUHO9A_xik',help_text='ONLY PHOTOS UPLOADED TO SERVER!!')
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='newsBlog_post')
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	objects = models.Manager() #Django's default model manager/filterer
	published = PublishedManager() #Our custom model manager/filterer
	tags = TaggableManager(through=UUIDTaggedItem)
	class Meta:
		ordering = ('-publish',)
	def __str__(self):
		 return self.title
	def get_absolute_url(self):
		 return reverse('newsBlog:detail',args=[self.publish.year,
		 										self.publish.month,
												self.publish.day, self.slug])

	def get_admin_url(self):
		return '/admin/newsBlog/post/'+self.pk+'/change/'


class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=150)
	body = models.TextField(blank=False)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	class Meta:
		ordering = ('-created',)
	def __str__(self):
		return f'Comment by {self.name} on {self.post}'
   