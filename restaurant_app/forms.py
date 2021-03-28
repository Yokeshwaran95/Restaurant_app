from django import forms
from restaurant_app.models import RestaurantLocation
from restaurant_app.validators import validate_category

class RestaurantCreateForm(forms.Form):
	name=forms.CharField(max_length=120)
	location=forms.CharField(required=False)
	Category=forms.CharField(required=False)



class RLCreateForm(forms.ModelForm):
	class Meta:
		model=RestaurantLocation
		fields=[
		"name","location","Category"]

