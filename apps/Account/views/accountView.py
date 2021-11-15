# imports of Django and  rest_framework
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# imports of serializers
from apps.Account.serializers import AccountSerializer

class accountCreate(generics.CreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    # def post(self, request, *args, **kwargs):
    #     """ Override POST method from generics.CreateAPIView class
    #     parameters:
    #         request: info data, provide by de HTTP method email

    #     Return:
    #         StringResponse with status code
    #     """
    #     serializer = accountSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return super().post(request, *args, **kwargs)

class accountDetail(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

class accountUpdate(generics.UpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):

        if (kwargs["type"] == "balance"):
            account = AccountSerializer.update_balance(request.data)
        elif (kwargs["type"] == "fields"):
            account = AccountSerializer.update_fields(request.data)
        else:
            stringResponse = {'detail': 'Invalid endpoint parameter'}
            return Response(stringResponse, status=status.HTTP_404_UNAUTHORIZED)
        print(account.to_representation())

        return Response(account.to_representation(), status=status.HTTP200_OK)