from django.urls import path
from . import views

urlpatterns = [
	path('register',views.register, name='register'),
	path('login',views.login, name='login'),
	path('logout',views.logout, name='logout'),
	path('homepage',views.homepage, name='homepage'),
	path('contact',views.contact, name='contact'),
	path('aboutus',views.aboutus, name='aboutus'),
	path('destination',views.destination, name='destination'),
]