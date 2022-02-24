from outlook_app.views.manager_dashboard.views import Experties
from django.views.generic import View
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from outlook_app import models
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# from outlook_app.forms import ChangeProfileFormAdmin
from django.contrib import messages

class RedirectToDashboardView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                url = reverse_lazy("admin:index")
            elif request.user.is_manager():
                url = reverse_lazy("manager_dashboard")
            elif request.user.is_hr():
                url = reverse_lazy("hr_dashboard")
            elif request.user.is_employee():
                url = reverse_lazy("employee_dashboard")
            else:
                url = reverse_lazy("applicant_job")
        else:
            all_experties = list(models.Experties.objects.values_list('experties', flat=True))
            all_jobs = models.Job.objects.filter(is_open=True, is_active=True)
            jobs = []
            for job in all_jobs:
                temp = {}
                temp['id'] = job.id
                temp['title'] = job.title
                temp['description'] = job.description
                temp['experience'] = job.get_experience_display
                temp['job_experties'] = list(models.Job.objects.filter(id=job.id).values_list('job_experties__experties', flat=True))
                jobs.append(temp)
            return render(request, "outlook/home.html", {'all_experties':all_experties, 'jobs':jobs})
        return redirect(url)