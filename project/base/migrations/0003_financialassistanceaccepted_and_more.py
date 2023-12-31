# Generated by Django 4.2.6 on 2023-10-31 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_collegestudentaccepted_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancialAssistanceAccepted',
            fields=[
                ('control_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('school_year', models.CharField(default='1st Years', max_length=50)),
                ('course', models.CharField(default='', max_length=50)),
                ('school', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAssistanceRejected',
            fields=[
                ('control_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('remarks', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialAssistanceRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_number', models.CharField(default='', max_length=50)),
                ('requirement', models.IntegerField(default=0)),
                ('req_a', models.CharField(default='False', max_length=100)),
                ('req_b', models.CharField(default='False', max_length=100)),
                ('req_c', models.CharField(default='False', max_length=100)),
                ('req_d', models.CharField(default='False', max_length=100)),
                ('req_e', models.CharField(default='False', max_length=100)),
                ('req_f', models.CharField(default='False', max_length=100)),
                ('req_g', models.CharField(default='False', max_length=100)),
                ('req_h', models.CharField(default='False', max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('control', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.financialassistanceapplication')),
            ],
        ),
    ]
