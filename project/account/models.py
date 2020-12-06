from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid 

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    emailVerified = models.BooleanField(default = False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token (sender, instance=None, created=False, **kwargs):
    if created:
    	Token.objects.create(user=instance)


def customPath(instance,filename):
	fileType = filename[(filename.rfind(".")+1):]
	return '{path}/{name}.{type}'.format(path='photos',name=uuid.uuid4(),type=fileType)

class Photos(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	photo = models.ImageField(upload_to=customPath)