# Generated by Django 3.2.6 on 2022-01-22 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlook_app', '0006_auto_20220122_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicantform',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
