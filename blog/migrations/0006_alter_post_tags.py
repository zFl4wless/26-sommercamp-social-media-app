# Generated by Django 4.2.3 on 2023-08-02 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.JSONField(default=list),
        ),
    ]
