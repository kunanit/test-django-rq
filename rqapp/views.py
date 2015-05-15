from django.shortcuts import render
from tasks import mytask
from django.http import HttpResponse
import django_rq
from time import sleep

# Create your views here.
def myview(request):
	
	job = django_rq.enqueue(mytask,'andrew')
	jobid = job.id
	q = django_rq.get_queue()
	print 'fetch 1'
	print q.fetch_job(jobid).result
	sleep(5)
	print 'fetch 2'
	print q.fetch_job(jobid).result
	return HttpResponse('hello world')