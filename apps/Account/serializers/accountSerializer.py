from rest_framework import serializers
from apps.Account.models import Account
from django.shortcuts import get_object_or_404

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def update_balance(valid_data):
        """ method for update balance for user account
        parameters:
            valid_data["id_cliente"]: ID account
            valid_data["balace"]: value of balance for increase in account
        return:
            account.this_account(): account representation
        """
        account = get_object_or_404(Account, id_client=valid_data["id_client"])
        account.balance += valid_data["balance"]
        account.save()
        return account.this_account()
    
    def update_fields(valid_data):
        """ method for update fields for user account
        parameters:
            valid_data["id_cliente"]: ID account
            valid_data["city"]: value of city to change
            valid_data["phone"]: value of phone to change
            valid_data["ages"]: value of ages to change
        return:
            account.this_account(): account representation
        """
        # eficient filter, return 404 if not found the account
        account = get_object_or_404(Account, id_client=valid_data["id_client"])
        account.city = valid_data["city"]
        account.phone = valid_data["phone"]
        account.ages = valid_data["ages"]
        account.save()
        return account.this_account()


    def to_representation(self, obj):
        account = Account.objects.get(id_client=obj.id_client)
        return {
            "id_account"      : account.id_account,
            "id_client"       : account.id_client,
            "city"            : account.city,
            "phone"           : account.phone,
            "ages"            : account.ages,
            "register_date"   : account.register_date,
            "balance"         : account.balance
        }

