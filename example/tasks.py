from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def sleepy(duration):
	sleep(duration)
	return None

@shared_task
def send_email_task():
	sleep(10)
	send_mail('Celery Task worked',
		'This is proof that task worked',
		'yokeshmathi6895@gmail.com',
		['yokesh.mathialagan@zf.com'])
	return None