from django.core.exceptions import ValidationError

def clean_name(value):
	email=value
	if "gmail" not in email:
		raise ValidationError("Not a valid Name")
	return email

CATEGORIES=['Indian','Chinese','Multicuisine', 'Arabian']

def validate_category(value):
	cap=value.capitalize()
	if not value in CATEGORIES and not cap in CATEGORIES:
		raise ValidationError(value+" is not a valid category")