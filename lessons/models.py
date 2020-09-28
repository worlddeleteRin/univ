from django.db import models
from django.utils.timezone import now
from datetime import datetime
import pytz
msc = pytz.timezone('Europe/Moscow')

# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length = 300, default = '')
    # imgurl = models.CharField(max_length = 2000, default = '')
    imgurl = models.ImageField(upload_to='static/images', null = True, blank = True)

    def __str__(self):
        return self.name 

class Subject(models.Model):
    name = models.CharField(max_length = 200, default = '')
    s_teacher = models.ManyToManyField(Teacher)
    # imgurl = models.CharField(max_length = 1000, default = 'https://placehold.it/500x500')
    imgurl = models.ImageField(upload_to='static/images', null = True, blank = True)

    def __str__(self):
        return self.name 

class Itemtypes(models.Model):
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, default = '')

    def __str__(self):
        return self.name 
        
class Item(models.Model):
    date = models.DateTimeField(blank=True, default = datetime.now(tz = msc),
    )
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    itype = models.ForeignKey(Itemtypes, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, default = '')
    itemurl = models.CharField(max_length = 2000, default = '')
    itemsize = models.CharField(max_length = 100, default = '')
    # imgurl = models.ImageField(upload_to='static/images', null = True, blank = True)
    # fileurl = models.FileField(upload_to='static/files')
    def __str__(self):
        return self.name 

    def time_from_create(self):
        data = self.date
        data = data.replace(tzinfo = None)
        time_now = datetime.now()
        time = time_now - data
        time_seconds = time.total_seconds()
        time_main = time_seconds / 60
        time_main = time_main / 60
        return time_main

def deleteall():
    t = Teacher.objects.all()
    t.delete()
    s = Subject.objects.all()
    s.delete()
    i = Item.objects.all()
    i.delete()
    t = Itemtypes.objects.all()
    t.delete()
    print('deleted all')


