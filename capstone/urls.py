from django.conf.urls import include, url
from django.contrib import admin
from truckapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^truckapp/', views.homepage, name='home'),
    url(r'^$', views.homepage, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^login_user/$', views.login_auth, name='auth'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^questionnaire/$', views.questionnaire, name='questionnaire'),
    url(r'^results/$', views.results, name='results'),
    url(r'^(<co_name>)-profile/$', views.co_profile, name='profile'),
    url(r'^(?P<co_name>)-contact/$', views.co_contact, name='contact'),
    url(r'^links/$', views.links, name='links'),
    url(r'^zip_form/$', views.zip_form, name='zip_form'),
    url(r'^distance/$', views.distance, name='distance'),
    url(r'^weather_form/$', views.weather_form, name='wetaher_form'),
    url(r'^search/$', views.search, name='search'),



]
