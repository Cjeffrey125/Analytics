# Generated by Django 4.2.6 on 2023-10-30 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegestudentaccepted',
            name='course',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='collegestudentaccepted',
            name='school',
            field=models.CharField(default='', max_length=50),
        ),
    ]
