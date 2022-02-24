from django import forms
from django.db.models import fields
from .models import *

class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description', 'requested_by', 'job_experties', 'experience', )

class AddExpertie(forms.ModelForm):
    class Meta:
        model = Experties
        fields = ('experties', )

class JobForm(forms.ModelForm):
    class Meta:
        model = ApplicantForm
        exclude = ('score', 'interviewer', 'interview_time', 'mcqsScore',)