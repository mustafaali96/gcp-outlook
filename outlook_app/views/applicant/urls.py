from django.urls import path, include

from outlook_app.views.applicant import views

urlpatterns = [
    path("", views.AllJobs.as_view(), name="applicant_job"),
    path("<job_id>/", views.Job.as_view(), name="job"),
]