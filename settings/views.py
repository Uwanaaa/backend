from django.shortcuts import render
from user.models import UserModel
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers import UserModelSerializer
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def profile(request):
    user_id = request.session.get('user_id')
    user = UserModel.objects.get(pk=user_id)

    if user is None:
        JsonResponse({"status":"User session is expired"})
    else:
        serialized_data = UserModelSerializer(user)
        password = request.session.get('password')

    data = {
        'data': serialized_data,
        'password': password
    }
    print(data)
    return JsonResponse(data)


def camera_deactivate(request):
    if request.method == 'GET':
        pass