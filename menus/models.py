from django.db import models
from django.conf import settings
from restaurant_app.models import RestaurantLocation
from django.urls import reverse
# Create your models here.

class Item(models.Model):
	#associations
	user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	restaurant=models.ForeignKey(RestaurantLocation,on_delete=models.CASCADE)

	#item stuff
	name = models.CharField(max_length=150)
	contents=models.TextField(help_text=
		"seperate each item by comma")
	excludes=models.TextField(blank=True, null=True,help_text=
		"seperate each item by comma")
	public=models.BooleanField(default=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse("Menu-Detail", kwargs={'pk':self.pk})

	def __str__(self):
		return self.name

	class Meta:
		ordering=["-updated","-timestamp"]

	def get_contents(self):
		return self.contents.split(",")

	def get_excludes(self):
		return self.excludes.split(",")