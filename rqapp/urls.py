from django.conf.urls import patterns, url
from rqapp import views

urlpatterns = patterns('',
	url(r'^myview/$', views.myview, name='myview'),
	url(r'^checkstatus/$', views.checkstatus, name='checkstatus'),
	url(r'^success/$', views.success, name='success'),

	)