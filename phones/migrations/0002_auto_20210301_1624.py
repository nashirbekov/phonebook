# Generated by Django 3.1.7 on 2021-03-01 10:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='phone',
            name='middlename',
        ),
        migrations.AddField(
            model_name='phone',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100, verbose_name='ФИО'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone',
            name='phonenumber',
            field=models.CharField(max_length=13, verbose_name='Номер'),
        ),
    ]