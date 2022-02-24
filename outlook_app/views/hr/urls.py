from django.urls import path, include

from outlook_app.views.hr import views

urlpatterns = [
    path("", views.Dashboard.as_view(), name="hr_dashboard"),
    path("job/<job_id>/", views.AllApplicants.as_view(), name="job_info"),
]