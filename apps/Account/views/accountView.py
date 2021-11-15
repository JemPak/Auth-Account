# imports of Django and  rest_framework
from rest_framework import generics, status
from rest_framework.response import Response
from apps.Account.models.account import Account

# shortcuts for HTTP response
from django.shortcuts import get_object_or_404

# imports of serializers
from apps.Account.serializers import AccountSerializer

class accountCreate(generics.CreateAPIView):
    serializer_class = AccountSerializer
    # the generics.CreateAPIVIEW method create a new account if the account not exist

class accountDetail(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get(self, request, *args, **kwargs):
        """ Override get method to retrive a Account  
        parameters:
            **kwargs: (key value) send by endpoint, we use pk to define id_client
                with this value, try to retrieve the account or HTTT_400 if not found
        Return:
            Account: information about the account  
        """
        
        # search the account with de pk parameter
        account = get_object_or_404(Account, id_client=kwargs["pk"])
        return Response(account.this_account(), status=status.HTTP_200_OK)


class accountUpdate(generics.UpdateAPIView):
    serializer_class = AccountSerializer # impor serializer class

    def put(self, request, *args, **kwargs):
        """ Override put method to update a value in the account
        parameters:
            **kwargs: (key value), the kwargs is used for define the type to update, it can be:
                update_balance: update only the balance field, add the new value balance 
                update_fields: update the fiels (ages, city, phone)
            request.data: dict with the values to update
                    
        Return:
                Account: information about the account
        """
        if (kwargs["type"] == "balance"):
            # validacion de que el balance sea mayor a 0
            if request.data["balance"] < 0:
                stringResponse = {'detail': 'Invalid balance'}
                return Response(stringResponse, status=status.HTTP_406_NOT_ACCEPTABLE)
            account = AccountSerializer.update_balance(request.data)
        elif (kwargs["type"] == "fields"):
            account = AccountSerializer.update_fields(request.data)
        else:
            stringResponse = {'detail': 'Invalid endpoint parameter'}
            return Response(stringResponse, status=status.HTTP_404_UNAUTHORIZED)
        return Response(account, status=status.HTTP_202_ACCEPTED)