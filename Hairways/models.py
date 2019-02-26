from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    nickname= models.CharField(max_length=30,null=True,blank=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nickname=models.CharField(max_length=30)
    email= models.CharField(max_length=30, default='myemail@gmail.com')


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ownerName = models.CharField(max_length=30)
    email = models.TextField(max_length=150)
    phone = models.PositiveIntegerField()
    password = models.CharField(max_length=25)

    def __str__(self):
        return self.ownerName


class Salons(models.Model):
    salonName = models.CharField(max_length=20)
    description = models.TextField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    Owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='my_salons')
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    status = models.BooleanField(default=0)
    shares = models.IntegerField(default=0)
    paybill = models.TextField(null=True, blank=True, max_length=12)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.salonName

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Likes(models.Model):
    salon = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name="salon_likes")
    def __str__(self):
        return self.salon.salonName

class Services(models.Model):
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='services')
    serviceName = models.CharField(max_length=100)
    serviceCost = models.CharField(max_length=50)
    serviceDuration = models.CharField(max_length=20)
    serviceBookings = models.IntegerField()
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.serviceName

class Appointments(models.Model):
    client= models.ForeignKey(User, on_delete=models.CASCADE, default=1,related_name='my_appointments')
    services = models.ManyToManyField(Services)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, default=1, related_name='appointments')
    AppointmentsStatus = models.BooleanField(default=False)
    date_time = models.DateTimeField()
    totalCost = models.IntegerField()

class Staff(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    date_started = models.DateTimeField()
    salary = models.IntegerField()
    favservice = models.CharField(max_length=100, null=True, blank=True)
    favclient = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.firstname

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_brand = models.CharField(max_length=100)
    salons = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name


class Comments(models.Model):
    salon = models.ForeignKey(Salons, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_comments')
    reply = models.TextField(max_length=250)
    created_date = models.DateTimeField(
        default=timezone.now
    )
    approved_comment = models.BooleanField(default=False)

    def __str__(self):
        return self.reply
    # to be revisited
    def approve(self):
        self.approved_comment = True
        self.save()
