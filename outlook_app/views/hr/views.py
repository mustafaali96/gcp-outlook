from outlook_app import models
from django.views.generic import View
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core.mail import EmailMultiAlternatives

import json
import pickle

class Dashboard(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        all_jobs = models.Job.objects.all()
        for job in all_jobs:
            applicants = models.ApplicantForm.objects.filter(job=job.id).count()
            job.applicants = applicants
        return render(request, "outlook/publish.html", {'all_jobs':all_jobs})

    def post(self, request, *args, **kwargs):
        job_status = request.POST.get("job_status")
        job_status = json.loads(job_status)
        if (models.Job.objects.get(id=job_status)).is_open==True:
            models.Job.objects.filter(id=job_status).update(is_open=False)
            return redirect('hr_dashboard')
        else:
            models.Job.objects.filter(id=job_status).update(is_open=True)
            return redirect('hr_dashboard')


class AllApplicants(View):
    @method_decorator(login_required)
    def get(self, request, job_id, *args, **kwargs):
        job = models.Job.objects.filter(id=job_id)[0]
        interviewers = models.UserProfile.objects.filter(role=3)

        # Load model
        model = pickle.load(open("model/finalized_model.sav", 'rb'))

        # Model Prediction Score Update
        newApplicants = models.ApplicantForm.objects.filter(job=job_id, score=-1)
        for newApplicant in newApplicants:
            score = model.predict([[newApplicant.experience, newApplicant.education, newApplicant.job.experience, newApplicant.applicant_experties.count()]])
            models.ApplicantForm.objects.filter(id=newApplicant.id).update(score=round(float(score),2))

        applicants = models.ApplicantForm.objects.filter(job=job_id).order_by('-score','-cv', 'id')
        return render(request, "outlook/all-applicants.html", 
                    {'job':job, 'applicants':applicants, 'interviewers':interviewers})

    def post(self, request, job_id, *args, **kwargs):
        try:
            interviewerId = request.POST.get("interviewer")
            interviewerId = json.loads(interviewerId)
            applicantId = request.POST.get("schedulingForId")
            applicantId = json.loads(applicantId)
            applicantInterviewDateTime = request.POST.get("interviewDateTime")

            models.ApplicantForm.objects.filter(id=applicantId).update(
                interviewer=interviewerId, interview_time=applicantInterviewDateTime)

            applicantDetails = models.ApplicantForm.objects.filter(id=applicantId)[0]
            mail_subject = f'Interview Schedule for {applicantDetails.job.title}'
            mail_msg = 'Important mail'
            html_content = f'<p>Dear <strong>{applicantDetails.name}</strong>,<br><br>Hope you are doing great.<br><br>Your Interview has been scheduled with {applicantDetails.interviewer.get_full_name()} on {applicantDetails.interview_time} for the position of {applicantDetails.job.title}.<br><br>You are requested to give quiz before your interview.<br><br> Quiz link: <a href="{applicantDetails.job.mcqs_link}">{applicantDetails.job.title} Quiz</a></p>'
            msg = EmailMultiAlternatives(mail_subject, mail_msg, '', [applicantDetails.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        except:
            pass
        
        job = models.Job.objects.filter(id=job_id)[0]
        applicants = models.ApplicantForm.objects.filter(job=job_id).order_by('-score', '-cv', 'id')
        interviewers = models.UserProfile.objects.filter(role=3)
        return render(request, "outlook/all-applicants.html", 
                    {'job':job, 'applicants' : applicants, 'interviewers' : interviewers})

        
