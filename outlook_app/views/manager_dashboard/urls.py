from django.urls import path, include

from outlook_app.views.manager_dashboard import views

urlpatterns = [
    path("", views.Dashboard.as_view(), name="manager_dashboard"),
    path("experties", views.Experties.as_view(), name="experties"),
]