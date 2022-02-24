from django.urls import path, include

from outlook_app.views.employee import views

urlpatterns = [
    path("", views.dashboard.as_view(), name="employee_dashboard"), 
    path("interview/all/", views.all_interviews.as_view(), name="employee_all_interviews"), 
    path("interview/past/", views.past_interviews.as_view(), name="employee_past_interviews"), 
]