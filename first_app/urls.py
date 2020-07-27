from django.urls import path
from .views import about
from .views import catalog
from .views import contacts
from .views import team
from .views import trash

urlpatterns = [
	path('about', about),
	path('catalog', catalog),
	path('contacts', contacts),
	path('team', team),
	path('trash', trash),
]
