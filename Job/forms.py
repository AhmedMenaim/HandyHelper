from django import forms
from django.db.models.query import QuerySet
from django.forms import models, widgets

from Job.models import Category, Job

class AddJobForm(forms.ModelForm):

    choice_list = (('Coding','Coding'),('Garden','Garden'),('Buying things','Buying things'),('Electronic','Electronic'),('Pet Care','Pet Care'),('Other','Other'))
    jobCategory = forms.MultipleChoiceField(choices=choice_list, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Job
        fields = ['jobTitle', 'jobDescribtion', 'jobLocation', 'jobCategory']

    def __init__(self, *args, **kwargs):
        super(AddJobForm, self).__init__(*args, **kwargs)
        self.fields['jobCategory'].queryset = Category.objects.all()
 

class EditJobForm(forms.ModelForm):

    choice_list = (('Coding','Coding'),('Garden','Garden'),('Buying things','Buying things'),('Electronic','Electronic'),('Pet Care','Pet Care'),('Other','Other'))
    
    jobCategory = forms.MultipleChoiceField(choices=choice_list, widget=forms.CheckboxSelectMultiple())

    class Meta:
         model = Job
         fields = ['jobTitle', 'jobDescribtion', 'jobLocation', 'jobCategory']


    
    def save(self, commit=True):
        job = self.instance
        job.jobTitle = self.cleaned_data['jobTitle']
        job.jobDescribtion = self.cleaned_data['jobDescribtion']
        job.jobLocation = self.cleaned_data['jobLocation']
        # breakpoint()
        job.jobCategory.set(self.cleaned_data['jobCategory'])

        if commit:
            job.save()
        return job


    # def clean_jobCategory(self):
    #     breakpoint()

    def validate(self, *args, **kwargs):
        data = dict(self.data)
        # job_categories = data.pop("jobCategory", [])
        
        self.data = data
        breakpoint()
        cleaned_data = super(EditJobForm, self).clean()
        # cleaned_data["jobCategory"] = job_categories
        breakpoint()

        return cleaned_data

    jobCategory = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    # def __init__(self, *args, **kwargs):
    #     super(EditJobForm, self).__init__(*args, **kwargs)
    #     self.fields['jobCategory'].queryset = Category.objects.all()
