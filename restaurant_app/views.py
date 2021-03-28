from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import random
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from restaurant_app.models import RestaurantLocation
from restaurant_app.forms import RestaurantCreateForm, RLCreateForm  




#--------------------------------------------------------------------------------------------------------------



class RestaurantListView(LoginRequiredMixin,ListView):
	template_name="restaurants/restaurant_list.html"
	login_url="/login/"
	queryset=RestaurantLocation.objects.all()
	def get_queryset(self):

		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantDetailedListView(LoginRequiredMixin,DetailView):
	template_name="restaurants/restaurant_detaillist.html"
	login_url="/login/"
	def get_queryset(self):

		return RestaurantLocation.objects.filter(owner=self.request.user)

class RestaurantLocationCreateView(LoginRequiredMixin,CreateView):
	form_class=RLCreateForm
	template_name="form.html"
	# success_url="/Restaurant-list/"
	login_url="/login/"
	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantLocationCreateView, self).form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context=super(RestaurantLocationCreateView,self).get_context_data(*args,**kwargs)
		context["title"]='Add Restaurant'
		return context

class RestaurantLocationUpdateView(LoginRequiredMixin,UpdateView):
	form_class=RLCreateForm
	template_name="form.html"
	# success_url="/Restaurant-list/"
	login_url="/login/"
	def form_valid(self,form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		return super(RestaurantLocationUpdateView, self).form_valid(form)

	def get_context_data(self,*args,**kwargs):
		context=super(RestaurantLocationUpdateView,self).get_context_data(*args,**kwargs)
		context["title"]='Update Restaurant'
		return context
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)



