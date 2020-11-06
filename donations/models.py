from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone

class Organization(models.Model):
    organization_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.organization_text


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200)

    def __str__(self):
        return self.task_text
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_bio = models.CharField(max_length=500)
    profile_location = models.CharField(max_length=100)
    profile_phone = models.CharField(max_length=100)
    favorite_orgs = models.ManyToManyField(Organization)
    # image = models.ImageField(upload_to='profile_image', blank=True)
"""
class Review(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    review_text = models.CharField(max_length=200000)
    pub_date = models.DateTimeField('date published') # auto_now_add=True
    def __str__(self):
        return self.review_text
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Product(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image_url = models.CharField(max_length=1000, null=True, blank=True)
	price = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.name
        