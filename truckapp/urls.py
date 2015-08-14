from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^questionnaire/$', views.questionnaire, name='questionnaire'),
    url(r'^results/$', views.results, name='results'),
    url(r'^(?P<co_name>)-profile/$', views.co_profile, name='profile'),
    url(r'^(?P<co_name>)-contact/$', views.co_contact, name='contact'),
    url(r'^links/$', views.links, name='links'),
    url(r'^distance/$', views.distance, name='distance'),


]