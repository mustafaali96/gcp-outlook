from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView
from outlook_app import home
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("auth/login/", LoginView.as_view(template_name="registration/login.html"), name="login_url"),
    path("auth/logout/", LogoutView.as_view(), name="logout_url"),

    # Home View
    path("", home.RedirectToDashboardView.as_view(), name="home"),

    # Reset password urls    
    path('reset/password/', auth_views.PasswordResetView.as_view(template_name='reset_password/forgot_password.html', html_email_template_name='reset_password/password_reset_email.html', extra_context={'hide_title': True}), name='password_reset'),   
    path('reset/password/done', auth_views.PasswordResetDoneView.as_view(template_name='reset_password/password_reset_done.html', extra_context={'hide_title': True}), name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset_password/confirm_email.html', extra_context={'hide_title': True}), name='password_reset_confirm'),    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password/completion_msg.html', extra_context={'hide_title': True}), name='password_reset_complete'),

    path("manager/", include("outlook_app.views.manager_dashboard.urls")),
    path("employee/", include("outlook_app.views.employee.urls")),
    path("hr/", include("outlook_app.views.hr.urls")),
    path("job/", include("outlook_app.views.applicant.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)