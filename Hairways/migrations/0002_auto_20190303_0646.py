# Generated by Django 2.0.9 on 2019-03-03 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hairways', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='password',
        ),
        migrations.AddField(
            model_name='owner',
            name='gender',
            field=models.CharField(default='Female', max_length=150),
        ),
        migrations.AddField(
            model_name='owner',
            name='location',
            field=models.CharField(default='Kisumu', max_length=25),
        ),
        migrations.AlterField(
            model_name='owner',
            name='email',
            field=models.CharField(max_length=150),
        ),
    ]
