from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import exceptions,status
from .models import User
from .serializers import UserSerializers
import jwt, datetime



# Create your views here.

class RegisterView(APIView):
  def post(self, request):
    serializer = UserSerializers(data = request.data)
    serializer.is_valid(raise_exception = True)
    serializer.save()
    return Response(serializer.data)


class LoginView(APIView):
  def post(self, request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username = username).first()

    if user is None:
      raise exceptions.AuthenticationFailed('User not found')

    if not user.check_password(password):
      raise exceptions.AuthenticationFailed('Incorrect credentials')

    payload = {
      "id":user.id,
      "exp":datetime.datetime.utcnow() + datetime.timedelta(hours=1),
      "iat":datetime.datetime.utcnow()

    }

    token =jwt.encode(payload, 'secret', algorithm='HS256') 

    response  = Response()
    response.set_cookie(key = "jwt", value= token, httponly=True)
    response.date = {
      "jwt":token,
    }
    
    return response


class UserView(APIView):
  # authentication_classes = [authentication.TokenAuthentication]
  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  def get(self, request):
    token = request.COOKIES.get('jwt')

    print("jwt:", token)

    if not token:
      raise exceptions.AuthenticationFailed('Unauthorized')

    try:

      payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise exceptions.AuthenticationFailed('Unauthorized')

    user = User.objects.filter(id = payload['id']).first()
    serializer = UserSerializers(user)
    
    return Response(serializer.data)



class LogoutView(APIView):

  def post(self, request):
    response = Response()
    response.delete_cookie('jwt')
    response.data ={
      "message":"successfully log out"
    }

    return response





    
