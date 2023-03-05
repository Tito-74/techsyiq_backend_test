from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.core.mail import send_mail
# from rest_framework import authentication
# from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import exceptions
from .models import TechsyiqTeam, EnrollmentApplication
from .serializers import TechsyiqTeamSerializers, EnrollmentApplicationSerializers
from rest_framework import filters
from rest_framework.decorators import api_view





class TechsyiqTeamView(APIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def post(self, request):
    if request.method == 'POST':
      serializer = TechsyiqTeamSerializers(data = request.data)
      print("data", serializer)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


  def get(self, request, *args, **kwargs):
    if request.method == 'GET':
      team = TechsyiqTeam.Object.all()

      serializer = TechsyiqTeamSerializers(team, many=True)

      return Response(serializer.data)
    

  
class TechsyiqTeamDetails(APIView):
  def get(self, request, *args, **kwargs):
    if request.method == 'GET':
      pk = kwargs.get('pk')

      try:
        team = TechsyiqTeam.objects.filter(id=pk).first()
      
      except TechsyiqTeam.DoesNotExist:
        return Response({"message":"Details does not exist"}, status = status.HTTP_404_NOT_FOUND)
      
      serializer = TechsyiqTeamSerializers(team)
    

      return Response(serializer.data)

  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def put(self, request, *args, **kwargs):
    if request.method == 'PUT':
      pk = kwargs.get('pk')

      try:
        team = TechsyiqTeam.objects.filter(id=pk).first()

      except TechsyiqTeam.DoesNotExist:
        return Response({"message":"details does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
      serializer = TechsyiqTeamSerializers(instance = team, data =request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
      
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def delete(self, request, *args, **kwargs):
    if request.method == 'DELETE':
      pk = kwargs.get('pk')

      try:
        team = TechsyiqTeam.objects.filter(id=pk).first()

      except TechsyiqTeam.DoesNotExist:
        return Response({"message":"details does not exist"}, status=status.HTTP_404_NOT_FOUND)

      team.delete()

      return Response({"message":"Deleted successfully"}, status=status.HTTP_200_OK)



class EnrollmentApplicationView(APIView):
  # def post(self, request):
   

  
  def get(self, request, *args, **kwargs):
    if request.method == 'GET':

      application = EnrollmentApplication.objects.all()

      serializer = EnrollmentApplicationSerializers(application, many=True)

      return Response(serializer.data)



class EnrollmentApplicationDetailsView(APIView):
  def get(self, request, *args, **kwargs):
    if request.method == 'GET':

      pk = kwargs.get('pk')

      try:
        application = EnrollmentApplication.objects.filter(id=pk).first()
      
      except EnrollmentApplication.DoesNotExist:
        return Response({"message":"Details does not exist"}, status = status.HTTP_404_NOT_FOUND)
      
      serializer = EnrollmentApplicationSerializers(application)
    

      return Response(serializer.data)


  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  def put(self, request, *args, **kwargs):
    if request.method == 'PUT':
      pk = kwargs.get('pk')

      try:
        application = EnrollmentApplication.objects.filter(id=pk).first()

      except EnrollmentApplication.DoesNotExist:
        return Response({"message":"details does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
      serializer = EnrollmentApplicationSerializers(instance = application, data =request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
      
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


  permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  def delete(self, request, *args, **kwargs):
    if request.method == 'DELETE':
      pk = kwargs.get('pk')

      try:
        application = EnrollmentApplication.objects.filter(id=pk).first()

      except EnrollmentApplication.DoesNotExist:
        return Response({"message":"details does not exist"}, status=status.HTTP_404_NOT_FOUND)

      application.delete()

      return Response({"message":"Deleted successfully"}, status=status.HTTP_200_OK)




 
@api_view(['POST'])
def enrollForTechsyicClass(request):
   if request.method == 'POST':
      print("hello done")

      serializer = EnrollmentApplicationSerializers(data = request.data)

      if serializer.is_valid():

        send_mail('Application Recieve','Your application was recieved and we are evaluating your documents.','kipkirui133@gmail.com',[request.data['email']], fail_silently = True)
        print("done sending mail")
        
        serializer.save()
        return Response(serializer.data)
       
      
      return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

