from django.shortcuts import render
from django.http import HttpResponse
from example.tasks import sleepy, send_email_task


# Create your views here.

def index(request):
	send_email_task.delay()
	# sleepy(10)
	return HttpResponse('Email sent with Celery!')
