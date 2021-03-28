
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (LoginView,PasswordResetView)
from restaurant_app.views import ( 
    RestaurantListView,
    RestaurantDetailedListView,
    RestaurantLocationCreateView,
    RestaurantLocationUpdateView
)
from menus.views import ( 
    ItemListView,
    ItemDetailView,
    ItemCreateView,
    ItemUpdateView
)
from django.views.generic import TemplateView
from example.views import (
    index)

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('forgot-password/',PasswordResetView.as_view(),name="password_reset"),
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="home.html"), name="home"),
    path('Restaurant-list/',RestaurantListView.as_view(),name="restaurantlist"),
    path('Restaurant-list/create/',RestaurantLocationCreateView.as_view(),name="Createrestaurantlist"),
    path('Restaurant-list/<slug>/edit/',RestaurantLocationUpdateView.as_view(),name="Updaterestaurantlist"),
    path('Restaurant-list/<slug>/',RestaurantDetailedListView.as_view(),name="Restaurant-Detail"),
    path('index/',index,name="index"),
    path('about/',TemplateView.as_view(template_name="about.html"),name="about"),
    path('contact/',TemplateView.as_view(template_name="contact.html"),name="contact"),
    path('items/',ItemListView.as_view(),name="menuslist"),
    path('items/create/',ItemCreateView.as_view(),name="CreateMenulist"),
    path('items/<pk>/',ItemDetailView.as_view(),name="Menu-Detail"),
    path('items/<pk>/edit',ItemUpdateView.as_view(),name="Menu-Update"),
]
