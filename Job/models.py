from django.db import models
from Users.models import Users
from django.db.models.signals import post_delete, pre_save, pre_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver

# Create your models here.


choice_list = (('Coding','Coding'),('Garden','Garden'),('Buying things','Buying things'),('Electronic','Electronic'),('Pet Care','Pet Care'),('Other','Other'))

class Category(models.Model):
    name = models.CharField(max_length = 20, choices=choice_list) #, error_messages={'unique':"There is a job under the same title"}
    is_checked = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name



# choices = Category.objects.all().values_list('name', 'name')
# choice_list = [choice for choice in choices]

class Job(models.Model):
    jobTitle               = models.CharField(max_length = 60, null=False, blank=False, unique=True, error_messages={'unique':"There is a job under the same title"})
    jobDescribtion         = models.TextField()
    jobLocation            = models.CharField(max_length = 60, null=False, blank=False)
    isAdded                = models.BooleanField(default = False)
    user                   = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #Just like refering to my user model which has been idintified before in settings, on_delete=models.CASCADE -> to remove everything related to it but not the user
    slug                   = models.SlugField(blank=True,unique=True) #just like url
    posted_on              = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    jobCategory            = models.ManyToManyField(to='Job.Category', related_name='jobs_related')
    # models.CharField(choices=choice_list, max_length = 60, default='Other')

    def __str__(self):
        return self.jobTitle

@receiver(post_delete, sender=Job)

def pre_save_job_receciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.user.username + "-" + instance.jobTitle)
        
pre_save.connect(pre_save_job_receciver, sender=Job)

