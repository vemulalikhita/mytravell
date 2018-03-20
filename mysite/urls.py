from django.conf.urls import url
from django.contrib import admin
from . import views

# ENSURE THAT URL PATTERNS ARE ALWAYS DIFFERENT IN EACH LINE TO AVOID CONFUSION

#/mysite/list/ list of the tours is dispalyed

urlpatterns = [

    url(r'^create/$', views.tour_create),  #mylist/create
url(r'^(?P<id>\d+)/$', views.tour_detail, name='detail'),
url(r'^list/$', views.tour_list, name='Tour-list'),
url(r'^(?P<id>\d+)/edit/$', views.tour_update, name='update'),
url(r'^(?P<id>\d+)/delete/$', views.tour_delete),

  #/mysite/touristcreate/ leads to creation of toursit

url(r'^touristcreate/$', views.tourist_create),
 url(r'^touristlogin/$', views.tourist_login, name='tourist_login'), #tourist login page saperate
url(r'^touristregister/$', views.tourist_register, name='tourist_register'),
url(r'^touristlogout/$', views.tourist_logout, name='tourist_logout'),
url(r'^touristdetail/(?P<id>\d+)/$', views.tourist_detail, name='tourist_detail'),
url(r'^touristlist/$', views.tourist_list, name='tourist_list'),
url(r'^touristdetail/(?P<id>\d+)/touristupdate/$', views.tourist_update, name='tourist_update'),        #to update the tourist details http://127.0.0.1:8000/mysite/tourists/touristdetail/1/touristupdate/
url(r'^touristdetail/(?P<id>\d+)/touristdelete/$', views.tourist_delete),
    url(r'^mysite/list/touristlogin/$', views.tourist_login, name='tourist_login'),  # tourist login page saperate
url(r'^mysite/touristlist/touristcreate/$', views.tourist_create, name='tourist_create'),


    url(r'^$', views.tour_list, name='list'),
]

