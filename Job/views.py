from django.shortcuts import get_object_or_404, redirect, render
from Job.models import Category, Job
from Job.forms import AddJobForm, EditJobForm
from Users.models import Users

# Create your views here.

def add_job_view (request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("Register")

    jobCategory = Job.jobCategory
    AddJob_form = AddJobForm(request.POST or None)
    if AddJob_form.is_valid():
        obj = AddJob_form.save(commit=False)
        job_user = Users.objects.filter(email=user.email).first()
        obj.user = job_user
        obj.save()
        jobCategory = request.POST.getlist('jobCategory') 
        for category in jobCategory:
            if Category.objects.all().exists():
                category = Category.objects.get(name=category)
                category.is_checked = True
                obj.jobCategory.add(category)
        context["Success_Message"] = "Job Added Successfully !!"
        AddJob_form = AddJobForm()
            
    context["jobCategory"] = jobCategory
    context['AddJob_form'] = AddJob_form
    return render(request,"AddJob.html", context )


def detail_job_view(request, slug):
    context = {}
    job = get_object_or_404(Job,slug=slug)
    context['job'] = job

    return render(request,"ViewJob.html", context)

def edit_job_view(request, slug):
    context = {}
    jobCategory = Job.jobCategory
    user = request.user
    if not user.is_authenticated:
        return redirect("Login")
    
    job = get_object_or_404(Job, slug=slug)
    # import pdb; pdb.set_trace()
    if request.POST:
        print(request.POST)
        # import pdb; pdb.set_trace()
        # data = request.POST
        # data["jobCategory"] = [1]
        form = EditJobForm(request.POST or None, instance=job)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            # obj = form.save()
            # jobCategory = request.POST.getlist('jobCategory') 
            # for category in jobCategory:
            #     import pdb; pdb.set_trace() 

            #     if Category.objects.all().exists():
            #         category = Category.objects.get(name=category)
            #         category.is_checked = True
            #         obj.jobCategory.add(category)
            #         print(category)
            # obj.save()
            # job = obj
            form.save() 
                    
            context["Success_Message"] = "Job Updated Successfully !!"


    
    form = EditJobForm(
        initial = {
            "jobTitle": job.jobTitle,
            "jobDescribtion": job.jobDescribtion,
            "jobLocation": job.jobLocation,
            "jobCategory": job.jobCategory,
        }
    )

    # context['jobCategory'] = jobCategory
    context['form'] = form
    return render(request,'EditJob.html', context )

def remove_job_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect("Register")
    Job.objects.filter(slug=slug).delete()
    return redirect("Dashboard")

def add_to_myjobs_view(request, slug):
    context = {}
    user = request.user
    context["Added_Message"] = "Job Added Successfully !!"
    if not user.is_authenticated:
        return redirect("Register")
    job = get_object_or_404(Job,slug=slug)
    job_user = Users.objects.filter(email=user.email).first()
    job.user = job_user
    job.isAdded = True
    job.save()
    return redirect("Dashboard")

def giveup_job_view(request, slug):
    context = {}
    user = request.user
    context["GivedUp"] = "Job has been given up Successfully !!"
    if not user.is_authenticated:
        return redirect("Register")
    job = get_object_or_404(Job,slug=slug)
    username = slug.split("-")[0]
    job_user = Users.objects.filter(username=username).first()
    job.user = job_user
    job.isAdded = False
    job.save()
    return redirect("Dashboard")
