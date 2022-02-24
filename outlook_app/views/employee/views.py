from outlook_app import models
from django.views.generic import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import json
import pygsheets
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives


class dashboard(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__gte=timezone.now()).order_by('interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})

    def post(self, request, *args, **kwargs):
        try:
            interviewId = request.POST.get("interviewId")
            interviewId = json.loads(interviewId)
            rating = request.POST.get("ratings")
            remarks = request.POST.get("remarks")

            models.ApplicantForm.objects.filter(id=interviewId).update(
                    recommendadtion=rating, remarks=remarks)
        except:
            pass

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__gte=timezone.now()).order_by('interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})


class all_interviews(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})

    def post(self, request, *args, **kwargs):
        try:
            interviewId = request.POST.get("interviewId")
            interviewId = json.loads(interviewId)
            rating = request.POST.get("ratings")
            remarks = request.POST.get("remarks")

            models.ApplicantForm.objects.filter(id=interviewId).update(
                    recommendadtion=rating, remarks=remarks)
        except:
            pass

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})


class past_interviews(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__lt=timezone.now()).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})

    def post(self, request, *args, **kwargs):
        try:
            interviewId = request.POST.get("interviewId")
            interviewId = json.loads(interviewId)
            rating = request.POST.get("ratings")
            remarks = request.POST.get("remarks")

            models.ApplicantForm.objects.filter(id=interviewId).update(
                    recommendadtion=rating, remarks=remarks)
        except:
            pass

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__lt=timezone.now()).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})