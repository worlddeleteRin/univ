from django import template

from lessons.models import * 

register = template.Library()

@register.simple_tag

def get_image_url(imgurl):
    if ('/' in imgurl.name):
        new_image = imgurl.name.split('/')[-1]
        return new_image
    else:
        return imgurl.name

@register.simple_tag
def get_corrent_time(time):
    return time
