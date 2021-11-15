from django.db import models
from apps.Auth.models import User

class Account(models.Model):
    id_account    = models.BigAutoField(primary_key=True)
    id_client     = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)
    city          = models.CharField("City", max_length=30)
    phone         = models.BigIntegerField("Phone")
    ages          = models.IntegerField("Age")
    register_date = models.DateField("Register Date", auto_now_add=True)
    balance       = models.BigIntegerField("Balance", default=0)
