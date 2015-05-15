from django.conf.urls import patterns, url
from rqapp import views

urlpatterns = patterns('',
	url(r'^myview$', views.myview, name='myview'),

	)