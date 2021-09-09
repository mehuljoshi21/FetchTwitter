from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('getTweetsByHashtag', views.getTweetsByHashtag, name='getTweetsByHashtag'),
    path('getTweetsByUserId', views.getTweetsByUserId, name='getTweetsByUserId'),
]
