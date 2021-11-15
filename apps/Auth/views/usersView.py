# imports of Django and  rest_framework 
from rest_framework import generics, status, views
from rest_framework.response import Response

# imports of simpleJWT 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# imports of models 
from apps.Auth.models.user import User
from apps.Auth.serializers.userSerializer import UserSerializer


class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        """ Override POST method from generics.RetrieveAPIView class
        parameters:
            request: info data, provide by de HTTP method email
            **kwargs: (key value) inside endponit

        Return:
            StringResponse with status code
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"email":request.data["email"], 
                     "password":request.data["password"]}

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
                
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED)

class UserDetailView(generics.RetrieveAPIView):
    # search for user with pk given, HTTP_404 if not found
    queryset = User.objects.all()
    serializer_class = UserSerializer

