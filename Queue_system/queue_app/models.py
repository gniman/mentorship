from django.db import models
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    contact = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=128)

class Fine_information(models.Model):

    user_id =models.ForeignKey(Users, on_delete=models.CASCADE,null=True ,blank=True)
    fine_amount = models.FloatField()
    fine_description = models.CharField(max_length=255)
    fine_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class queue_info(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    queue_position = models.IntegerField()
    queue_data = models.DateTimeField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class notification(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    message = models.CharField(max_length=255)
    date_time = models.DateTimeField()
    notification_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class payment(models.Model):
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE,null=True,blank=True)
    payment_amount = models.FloatField()
    payment_date = models.DateTimeField()
    payment_status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
