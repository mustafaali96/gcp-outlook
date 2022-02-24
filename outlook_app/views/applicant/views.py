from outlook_app import forms, models
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

import json

class AllJobs(View):
    def get(self, request, *args, **kwargs):
        all_jobs = models.Job.objects.filter(is_open=True, is_active=True)
        return render(request, "outlook/applicant-jobs.html", {'all_jobs': all_jobs})


class Job(View):
    def get(self, request, job_id, *args, **kwargs):
        job = models.Job.objects.get(id=job_id)
        experties = models.Experties.objects.all()
        applicant_form = forms.JobForm()
        return render(request, "outlook/applicant-form.html", {'applicant_form': applicant_form, 'job':job, 'experties':experties})

    def post(self, request, job_id, *args, **kwargs):
        job = models.Job.objects.get(id=job_id)
        applicant_form = forms.JobForm(request.POST, request.FILES)
        if applicant_form.is_valid():
            applicant_form.save()
            return redirect("home")
        else:
            return HttpResponse("""You have already applied for this job. <a href ='../%s/'>reload</a>"""%(job_id))
        return render(request, "outlook/applicant-form.html", {'applicant_form': applicant_form, 'job':job})

