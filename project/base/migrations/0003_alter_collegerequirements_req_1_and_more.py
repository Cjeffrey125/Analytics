# Generated by Django 4.2.6 on 2023-10-17 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_collegerequirements_control_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegerequirements',
            name='req_1',
            field=models.CharField(default='True', max_length=100),
        ),
        migrations.AlterField(
            model_name='collegerequirements',
            name='req_2',
            field=models.CharField(default='True', max_length=100),
        ),
    ]