from django.db import models

class Account(models.Model):
    id_account    = models.BigAutoField(primary_key=True)
    id_client     = models.IntegerField("user_id", unique=True, db_index=True)
    city          = models.CharField("City", max_length=30)
    phone         = models.BigIntegerField("Phone")
    ages          = models.IntegerField("Age")
    register_date = models.DateField("Register Date", auto_now_add=True)
    balance       = models.BigIntegerField("Balance", default=0)

    def this_account(self):
        # Recursive method to get the data account
        return {                            
            "id_account": self.id_account,
            "id_client": self.id_client,
            "city": self.city,
            "phone": self.phone,
            "ages": self.ages,
            "register_date": self.register_date,
            "balance": self.balance
        }
