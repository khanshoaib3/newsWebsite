from django import template
from django.contrib.auth.models import Group
from datetime import datetime
from django.utils.timezone import utc

register = template.Library()

@register.filter(name="time_difference")
def time_difference(post):
    now = datetime.utcnow().replace(tzinfo=utc)
    timediff = now - post.publish
    diff = int(timediff.total_seconds())
    if diff<3600:
        return str(int(diff/60)) + " minutes ago"
    elif diff>=3600 and diff<86400:
        return str(int(diff/3600)) + " hours ago"
    elif diff>=86400:
        min = diff
        while(min>=86400):
            min = min - 86400
        min = min/(3600)
        return str(int(diff/86400)) + " day "+str(int(min))+" hours ago"