from rest_framework import serializers
from apps.Auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, obj):
        """
            representation obj to return 
        """
        print(dir(obj))
        user = User.objects.get(id_user=obj.id_user)
        return {
                'id_client': user.id_user, 
                'name': user.name,
                'email': user.email,
                'nit': user.nit,
                'is_admin': user.is_superuser,
                }