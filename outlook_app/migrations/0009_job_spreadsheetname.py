# Generated by Django 3.2.6 on 2022-02-08 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('outlook_app', '0008_auto_20220129_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='spreadSheetName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
