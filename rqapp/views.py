from django.shortcuts import render
from tasks import mytask
from django.http import HttpResponse
import django_rq
from time import sleep

# Create your views here.
def myview(request):
	if request.method == 'POST':
		name = request.POST['name']
		job = django_rq.enqueue(mytask,name)
		return HttpResponse(job.id)
	else:
		return render(request,'rqapp/testpage.html')

def checkstatus(request):
	jobid = request.GET['jobid']
	q = django_rq.get_queue()
	print 'checking for results...'
	if q.fetch_job(jobid).result:

		return HttpResponse('done')
	else:
		return HttpResponse('processing')

def success(request):
	jobid = request.GET['jobid']
	q = django_rq.get_queue()
	result = q.fetch_job(jobid).result
	return HttpResponse(result)

def uploadfile(request):
	if request.method == 'POST':
		f = request.FILES['file']
		print f
		return HttpResponse('thanks')
	else:
		return render(request, 'rqapp/uploadfile.html')
