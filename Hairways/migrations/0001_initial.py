# Generated by Django 2.1.5 on 2019-02-14 18:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('AppointmentsId', models.IntegerField(primary_key=True, serialize=False)),
                ('AppointmentsStatus', models.BooleanField()),
                ('date_time', models.DateTimeField()),
                ('totalCost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('reply', models.TextField(max_length=250)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('ownerId', models.IntegerField(primary_key=True, serialize=False)),
                ('ownerName', models.CharField(max_length=30)),
                ('email', models.TextField(max_length=150)),
                ('phone', models.PositiveIntegerField()),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('productId', models.IntegerField(primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('product_brand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salonName', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('views', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=True)),
                ('shares', models.IntegerField(blank=True, null=True)),
                ('paybill', models.TextField(blank=True, max_length=12, null=True)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('serviceId', models.IntegerField(primary_key=True, serialize=False)),
                ('serviceName', models.CharField(max_length=100)),
                ('serviceCost', models.CharField(max_length=50)),
                ('serviceDuration', models.CharField(max_length=20)),
                ('serviceBookings', models.IntegerField()),
                ('svailability', models.BooleanField(default=True)),
                ('salons', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Salons')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_client', models.BooleanField(default=False)),
                ('is_owner', models.BooleanField(default=False)),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nickname', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='salons',
            name='Owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salons',
            name='ownerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Owners'),
        ),
        migrations.AddField(
            model_name='products',
            name='salons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Salons'),
        ),
        migrations.AddField(
            model_name='pictures',
            name='salonId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Salons'),
        ),
        migrations.AddField(
            model_name='comments',
            name='salon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Hairways.Salons'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='salons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Salons'),
        ),
        migrations.AddField(
            model_name='appointments',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hairways.Services'),
        ),
    ]
