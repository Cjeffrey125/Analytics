# Generated by Django 4.2.6 on 2023-10-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_collegestudentaccepted_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegestudentrejected',
            name='course',
        ),
        migrations.RemoveField(
            model_name='collegestudentrejected',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='collegestudentrejected',
            name='remarks',
        ),
        migrations.RemoveField(
            model_name='collegestudentrejected',
            name='school',
        ),
        migrations.RemoveField(
            model_name='collegestudentrejected',
            name='school_year',
        ),
        migrations.AlterField(
            model_name='collegestudentaccepted',
            name='school_year',
            field=models.CharField(default='1st Years', max_length=50),
        ),
    ]