from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
def home(request):
    return render(request, 'jobs/home.html')