# Generated by Django 4.2.3 on 2023-08-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_profile_pic_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='uploads'),
        ),
    ]
