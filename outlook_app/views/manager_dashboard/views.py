from django.db.models import fields
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from outlook_app import models, forms
import json

class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        job_form = forms.AddJobForm()
        experties = models.Experties.objects.all()
        all_jobs = models.Job.objects.all()
        return render(request, "outlook/jobs.html", {'job_form': job_form, 'experties':experties, 'all_jobs':all_jobs})

    def post(self, request, *args, **kwargs):
        job_form = forms.AddJobForm(request.POST)
        experties = models.Experties.objects.all()
        all_jobs = models.Job.objects.all()
        try:
            job_status = request.POST.get("job_status")
            job_status = json.loads(job_status)
            if (models.Job.objects.get(id=job_status)).is_active==True:
                models.Job.objects.filter(id=job_status).update(is_active=False, is_open=False)
            else:
                models.Job.objects.filter(id=job_status).update(is_active=True)
            return redirect('manager_dashboard')
        except:pass
        if job_form.is_valid():
            job_form.save()
            return redirect('manager_dashboard')
        return render(request, "outlook/jobs.html", {'job_form': job_form, 'experties':experties, 'all_jobs':all_jobs})

class Experties(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        expertie_form = forms.AddExpertie()
        experties = models.Experties.objects.all()
        return render(request, "outlook/experties.html", {'expertie_form':expertie_form, 'experties':experties})

    def post(self, request, *args, **kwargs):
        expertie_form = forms.AddExpertie(request.POST)
        experties = models.Experties.objects.all()
        if expertie_form.is_valid():
            expertie_form.save()
            return redirect('experties')
        return render(request, "outlook/experties.html", {'expertie_form':expertie_form, 'experties':experties})