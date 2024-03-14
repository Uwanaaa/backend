from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer


usermodel = get_user_model()

class UserModelSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = usermodel
        fields = ['id','email','first_name','last_name','password','mobile_number']

