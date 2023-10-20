# Generated by Django 4.2.6 on 2023-10-20 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_collegerequirements_approved_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegerequirements',
            old_name='req_1',
            new_name='req_a',
        ),
        migrations.RenameField(
            model_name='collegerequirements',
            old_name='req_2',
            new_name='req_b',
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_c',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_d',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_e',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_f',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_g',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_h',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_i',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_j',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_k',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_l',
            field=models.CharField(default='False', max_length=100),
        ),
        migrations.AddField(
            model_name='collegerequirements',
            name='req_m',
            field=models.CharField(default='False', max_length=100),
        ),
    ]
