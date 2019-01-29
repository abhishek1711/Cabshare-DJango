from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
from django.db.models.signals import post_save


places = (
('COLLEGE-DANAPUR','COLLEGE-DANAPUR'),
('COLLEGE-PATNA STATION','COLLEGE-PATNA STATION'),
('COLLEGE-PATNA AIRPOR','COLLEGE-PATNA AIRPORT'),
('DANAPUR-COLLEGE','DANAPUR-COLLEGE'),
('PATNA AIRPORT-COLLEGE','PATNA AIRPORT-COLLEGE'),
('PATNA STATION-COLLEGE','PATNA STATION-COLLEGE'),

)

class UserProfileManager(models.Manager):
    pass

#
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100,default='')
    city = models.CharField(max_length=100,default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=10,default=0)
    # image = models.ImageField(upload_to='profile_image',blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)


class Post(models.Model):

    fir = models.CharField(max_length=100,default='')

    route = models.CharField(max_length=100,choices=places,default='COLLEGE')
    # person = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    phone_no = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # user = models.ForeignKey(User,on_delete=models.CASCADE)
