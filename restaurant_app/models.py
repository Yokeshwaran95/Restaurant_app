from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from restaurant_app.utils import unique_slug_generator
from restaurant_app.validators import validate_category
from django.urls import reverse
# Create your models here.
User=settings.AUTH_USER_MODEL
class RestaurantLocation(models.Model):
	owner=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=120)
	location=models.CharField(max_length=120,null=True,blank=True)
	Category=models.CharField(max_length=120,null=True,blank=False,validators=[validate_category])
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	slug=models.SlugField(null=True,blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("Restaurant-Detail", kwargs={'slug':self.slug})

	@property
	def title(self):
		return self.name

def rl_pre_save_receiver(sender,instance, *args, **kwargs):
	print('saving...')
	print(instance.timestamp)
	if not instance.slug:
		instance.slug=unique_slug_generator(instance)

def rl_post_save_receiver(sender,instance, *args, **kwargs):
	print('saved...')
	print(instance.timestamp)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

# post_save.connect(rl_post_save_receiver, sender=RestaurantLocation)