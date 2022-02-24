# Generated by Django 3.1.5 on 2021-09-05 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('outlook_app', '0002_applicantform'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantform',
            name='interview_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='applicantform',
            name='interviewer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interviewer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applicantform',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]