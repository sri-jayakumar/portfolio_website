from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.order_by('-calendar')
    return render(request, 'projects/index.html', {'jobs' : jobs})

def detail(request, job_id):
    jobs = Job.objects.order_by('-calendar')
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'projects/detail.html', {'job' : job_detail, 'jobs' : jobs})

