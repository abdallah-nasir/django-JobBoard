# Generated by Django 3.0.7 on 2020-10-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20201020_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default=1, upload_to='image_upload'),
            preserve_default=False,
        ),
    ]
