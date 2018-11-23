# Generated by Django 2.0.9 on 2018-11-23 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Hairways', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoiments',
            name='AppoimentsStatus',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='owners',
            name='OwnerName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='owners',
            name='Phone',
            field=models.PositiveIntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='salons',
            name='CommentsId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hairways.Comments'),
        ),
        migrations.AlterField(
            model_name='salons',
            name='Likes',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salons',
            name='Paybill',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='salons',
            name='ServiceId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Hairways.Services'),
        ),
        migrations.AlterField(
            model_name='salons',
            name='Views',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='ServiceCost',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='ServiceName',
            field=models.CharField(max_length=100),
        ),
    ]
