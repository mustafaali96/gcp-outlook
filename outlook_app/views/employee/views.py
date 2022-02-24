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

        newApplicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__gte=timezone.now(), mcqsScore=-1)
        
        if len(newApplicants) > 0:
            for newApplicant in newApplicants:
                client = pygsheets.authorize(service_file='model/optimal-relic-341015-95443ddcd5b0.json') #ssuet account
                try:
                    sh = client.open(newApplicant.job.spreadSheetName).sheet1
                    data = sh.get_all_records()
                    for record in data:
                        if record["Email Address"] == newApplicant.email:
                            score = record["Score"].split("/")
                            score = int(score[0]) #/ int(score[1])
                            models.ApplicantForm.objects.filter(id=newApplicant.id).update(mcqsScore=score)
                except:
                    continue

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
            applicantId = request.POST.get("applicantId")
            applicantDetails = models.ApplicantForm.objects.filter(id=applicantId)[0]

            mail_subject = f'Quiz for {applicantDetails.job.title}'
            mail_msg = 'Important mail'
            html_content = f'<p>Dear <strong>{applicantDetails.name}</strong>,<br><br>Your Interviewer {applicantDetails.interviewer.get_full_name()} requested you to take quiz before {applicantDetails.interview_time} for the smooth interview process.<br><br> Quiz link: <a href="{applicantDetails.job.mcqs_link}">{applicantDetails.job.title} Quiz</a></p>'
            msg = EmailMultiAlternatives(mail_subject, mail_msg, 'outlook360ssuet@gmail.com', [applicantDetails.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__gte=timezone.now()).order_by('interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})


class all_interviews(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        newApplicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, mcqsScore=-1)
        if len(newApplicants) > 0:
            for newApplicant in newApplicants:
                client = pygsheets.authorize(service_file='model/optimal-relic-341015-95443ddcd5b0.json') #ssuet account
                try:
                    sh = client.open(newApplicant.job.spreadSheetName).sheet1
                    data = sh.get_all_records()
                    for record in data:
                        if record["Email Address"] == newApplicant.email:
                            score = record["Score"].split("/")
                            score = int(score[0]) #/ int(score[1])
                            models.ApplicantForm.objects.filter(id=newApplicant.id).update(mcqsScore=score)
                except:
                    continue

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
            applicantId = request.POST.get("applicantId")
            applicantDetails = models.ApplicantForm.objects.filter(id=applicantId)[0]

            mail_subject = f'Quiz for {applicantDetails.job.title}'
            mail_msg = 'Important mail'
            html_content = f'<p>Dear <strong>{applicantDetails.name}</strong>,<br><br>Your Interviewer {applicantDetails.interviewer.get_full_name()} requested you to take quiz before {applicantDetails.interview_time} for the smooth interview process.<br><br> Quiz link: <a href="{applicantDetails.job.mcqs_link}">{applicantDetails.job.title} Quiz</a></p>'
            msg = EmailMultiAlternatives(mail_subject, mail_msg, 'outlook360ssuet@gmail.com', [applicantDetails.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})


class past_interviews(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        newApplicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__lt=timezone.now(), mcqsScore=-1)
        if len(newApplicants) > 0:
            for newApplicant in newApplicants:
                client = pygsheets.authorize(service_file='model/optimal-relic-341015-95443ddcd5b0.json') #ssuet account
                try:
                    sh = client.open(newApplicant.job.spreadSheetName).sheet1
                    data = sh.get_all_records()
                    for record in data:
                        if record["Email Address"] == newApplicant.email:
                            score = record["Score"].split("/")
                            score = int(score[0]) #/ int(score[1])
                            models.ApplicantForm.objects.filter(id=newApplicant.id).update(mcqsScore=score)
                except:
                    continue

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
            applicantId = request.POST.get("applicantId")
            applicantDetails = models.ApplicantForm.objects.filter(id=applicantId)[0]

            mail_subject = f'Quiz for {applicantDetails.job.title}'
            mail_msg = 'Important mail'
            html_content = f'<p>Dear <strong>{applicantDetails.name}</strong>,<br><br>Your Interviewer {applicantDetails.interviewer.get_full_name()} requested you to take quiz before {applicantDetails.interview_time} for the smooth interview process.<br><br> Quiz link: <a href="{applicantDetails.job.mcqs_link}">{applicantDetails.job.title} Quiz</a></p>'
            msg = EmailMultiAlternatives(mail_subject, mail_msg, 'outlook360ssuet@gmail.com', [applicantDetails.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

        applicants = models.ApplicantForm.objects.filter(interviewer=request.user.id, interview_time__lt=timezone.now()).order_by('-interview_time')
        return render(request, "outlook/interviews.html", {'applicants':applicants})