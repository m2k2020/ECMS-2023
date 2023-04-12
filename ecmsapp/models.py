from django.db import models

# Create your models here.

# --------------- User Account -----------------
class Users(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=7)
    tell = models.CharField(max_length=15)
    username = models.CharField(max_length=15)   
    password = models.CharField(max_length=15)
    active = models.BooleanField(default=True) # True if we are active Else False to disable
    status = models.IntegerField(default=0) # status 0 means this one is active while 1 = inactive user

# --------------- House Table -----------------
class House(models.Model):
    district =models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    houseno = models.IntegerField()
    status = models.IntegerField(default=0) # default 0 is reserved for Active while 1 is reserved for Deleted


# --------------- Renter Table -----------------
class Renter(models.Model):
    name = models.CharField(max_length=25)
    tell = models.CharField(max_length=15)
    martial_status = models.CharField(max_length=15)
    status = models.IntegerField(default=0) # default 0 is Active while 1 is deleted

# --------------- Enviroment Table -----------------
class Enviroment(models.Model):
    house_id = models.ForeignKey(House, on_delete=models.CASCADE)
    renter_id = models.ForeignKey(Renter, on_delete=models.CASCADE)
    regoster_date = models.DateField()
    status = models.IntegerField(default=0) # default 0 is Active and 1 is deactivated

# --------------- Service Table -----------------
class Service(models.Model):
    enviroment_id = models.ForeignKey(Enviroment,on_delete=models.CASCADE)
    date = models.DateField()
    status = models.IntegerField(default=0) # default 0 is active and 1 is deactivated

# --------------- Transaction Table -----------------
class Transaction(models.Model):
    service_id = models.ForeignKey(Service,on_delete= models.CASCADE)
    account = models.CharField(max_length=7)
    price = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField(default=0) # default 0 is active and 1 is deactivated