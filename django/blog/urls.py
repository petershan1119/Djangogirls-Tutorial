from django.urls import path
#from blog import views
from . import views

urlpatterns = [
    path('', views.post_list),
]
