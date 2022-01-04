from django.shortcuts import render
from django.http import HttpResponse
# from HandyHelperDjango.models import User
from Job.models import Job

# Create your views here.


# def Register(request):
#     return render(request, 'Register.html')


def Dashboard(request):
    jobs = Job.objects.all()
    return render(request, 'Dashboard.html', {"jobs": jobs})
  

def ViewJob(request):
    return render(request, 'ViewJob.html')


