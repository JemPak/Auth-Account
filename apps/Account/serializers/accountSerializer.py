from rest_framework import serializers
from apps.Account.models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def update_balance(self, valid_data):
        account = Account.objects.get(id_client=valid_data["id_client"])
        account.balance += valid_data["balance"]
        account.save()
        return account
    
    def update_fields(self, valid_data):
        account = Account.objects.get(id_client=valid_data["id_client"])
        account.city = valid_data["city"]
        account.phone = valid_data["phone"]
        account.ages = valid_data["ages"]
        account.save()
        return account


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

