# Generated by Django 3.0.7 on 2020-10-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_delete_company'),
        ('home', '0002_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='jobs',
        ),
        migrations.AddField(
            model_name='company',
            name='jobs',
            field=models.ManyToManyField(to='job.Job'),
        ),
    ]
