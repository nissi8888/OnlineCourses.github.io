# Generated by Django 5.0.2 on 2024-02-11 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_rename_dicount_course_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
