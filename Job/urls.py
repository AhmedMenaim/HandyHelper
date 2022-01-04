from django.urls import path
from django.urls.resolvers import URLPattern


from Job.views import (

    add_job_view,
    detail_job_view,
    edit_job_view,
    remove_job_view,
    add_to_myjobs_view,
    giveup_job_view,
) 

app_name = 'Job'

urlpatterns = [
    path('AddJob', add_job_view, name="AddJob"),
    path('<slug>/', detail_job_view, name="ViewJob"),
    path('<slug>/edit', edit_job_view, name="EditJob"),
    path('<slug>/remove', remove_job_view, name="RemoveJob"),
    path('<slug>/addtomyjobs', add_to_myjobs_view, name="AddToMyJobs"),
    path('<slug>/giveupjob', giveup_job_view, name="GiveUpJob"),
]