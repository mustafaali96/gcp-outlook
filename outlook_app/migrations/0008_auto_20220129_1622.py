# Generated by Django 3.2.6 on 2022-01-29 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlook_app', '0007_alter_applicantform_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicantform',
            name='mcqsScore',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='mcqs_link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='mcqs_score',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
