from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):

    # user type
    MANAGER = 1
    HR = 2
    EMPLOYEE = 3
    ROLE_CHOICES = (
        (MANAGER, "Manager"),
        (HR, "HR"),
        (EMPLOYEE, "Employee"),
    )

    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    username = models.CharField(max_length=64, null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    contact = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)
    # is_superuser = models.BooleanField(default=False)
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, default=3)
    job_experties = models.ManyToManyField("Experties", blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'role']


    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return f'{self.first_name}'

    def __str__(self):
        return f"{self.get_full_name()} | {self.username}" 

    def is_manager(self):
        return self.role == 1
    
    def is_hr(self):
        return self.role == 2
    
    def is_employee(self):
        return self.role == 3


class Experties(models.Model):
    experties = models.CharField(max_length=100, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.experties


class Job(models.Model):
    # Experience Required
    INTERNSHIP = 0
    FRESH = 1
    MID = 2
    SENIOR =3
    EXPERT =4

    EXPERIENCE_CHOICES = (
        (INTERNSHIP, "Internship"),
        (FRESH, "0-1 Year"),
        (MID, "1-3 Years"),
        (SENIOR, "3-5 Years"),
        (EXPERT, "5+ Years"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    requested_by = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=False, blank=False, related_name='requested_by')
    posted_by = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=True, blank=True, related_name='posted_by')
    job_experties = models.ManyToManyField("Experties", blank=True)
    experience = models.SmallIntegerField(choices=EXPERIENCE_CHOICES, default=1)
    is_active = models.BooleanField(default=True)    # Manager Posted new Job Request
    is_open = models.BooleanField(default=False)    # HR accepting new candidate
    spreadSheetName = models.CharField(max_length=50, blank=True, null=True)
    mcqs_link = models.CharField(max_length=255, blank=True, null=True)
    mcqs_score = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.requested_by} | {self.experience}" 


class ApplicantForm(models.Model):
    UNDERGRADUATE = 0
    Bachelors = 1
    Masters = 2
    PhD =3

    EDUCATION_CHOICES = (
        (UNDERGRADUATE, "Undergraduate"),
        (Bachelors, "Bachelors"),
        (Masters, "Masters"),
        (PhD, "PhD"),
    )

    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    contact = models.CharField(max_length=15)
    cv = models.FileField(upload_to="CVs/", null=True, blank=True)
    job = models.ForeignKey("Job", on_delete=models.CASCADE, null=False, blank=False)
    applicant_experties = models.ManyToManyField("Experties", blank=True)
    education = models.SmallIntegerField(choices=EDUCATION_CHOICES, default=0)
    experience = models.FloatField(null=False, blank=False, default=0)
    score = models.FloatField(null=True, blank=True, default=-1)
    mcqsScore = models.FloatField(null=True, blank=True, default=-1)
    interviewer = models.ForeignKey("UserProfile", on_delete=models.CASCADE, null=True, blank=True, related_name='interviewer')
    interview_time = models.DateTimeField(null=True, blank=True)
    recommendadtion = models.CharField(max_length=25, null=True, blank=True)
    remarks = models.CharField(max_length=100, null=True, blank=True)


    class Meta:
        unique_together = ("email", "job")

    def __str__(self):
        return f"{self.name} | {self.job} | {self.email}" 

