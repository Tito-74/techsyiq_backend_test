from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
# from django.core.mail import send_mail
# from rest_framework import authentication
# from django.shortcuts import get_object_or_404
from rest_framework import status
# from rest_framework import exceptions
from .models import Category, Blog
from .serializers import CategorySerializers, BlogSerializers
from rest_framework import filters
from rest_framework.decorators import api_view


class CategoryView(APIView):
  
  def post(self, request):
    serializer = CategorySerializers(data = request.data)
    if serializer.is_valid():
      serializer.save()
    return Response(serializer.data)
  

  def get(self, request):
    category = Category.objects.all()
    serializer = CategorySerializers(category, many=True)

    return Response(serializer.data)


  # def get(self, request, *arg, **kwargs):
  #   pk = kwargs.get('pk')
  #   category = get_object_or_404(Category.objects.all(), pk=pk)
    
  #   serializer = CategorySerializers(category)

  #   return Response(serializer.data)
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def put(self, request, *arg, **kwargs):
    pk = kwargs.get('pk')

    try:
    
      category = Category.objects.get(id=pk)

    except Category.DoesNotExist:
      return Response({"message":"Category does not exist"},status = status.HTTP_404_NOT_FOUND)

    serializer = CategorySerializers(instance =category, data = request.data)
    if serializer.is_valid():
      serializer.save()
    
    return Response(serializer.data) 


  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def delete(self, *args, **kwargs):
    pk = kwargs.get('pk')

    try:
    
      category = Category.objects.get(id=pk)

    except Category.DoesNotExist:
      return Response({"message":"Category does not exist"},
      status = status.HTTP_404_NOT_FOUND)

    category.delete()

    return Response({"message":"Category deleted"})



class BlogView(APIView):
  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def post(self, request):
    serializer = BlogSerializers(data = request.data)
    # print("data", serializer)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)


  def get(self, request, *args, **kwargs):
    if request.method == 'GET':
      blog = Blog.objects.all()

      serializer = BlogSerializers(blog, many=True)
      
      return Response(serializer.data)


class BlogDetailsView(APIView):
  def get(self, request, *args, **kwargs):
    if request.method == 'GET':
      pk = kwargs.get('pk')

      blog = Blog.objects.get(id=pk)

      serializer = BlogSerializers(blog)

      return Response(serializer.data)

  permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  def put(self, request, *args, **kwargs):
    if request.method == 'PUT':
      pk = kwargs.get('pk')

      try:
        blog = Blog.objects.get(id=pk)
      
      except Blog.DoesNotExist:
        return Response({"message":"Blog does not exist"}, status=status.HTTP_404_NOT_FOUND)

      serializer = BlogSerializers(instance=blog, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
      return Response(serializer.error, status=status.HTTP_200_OK)

  def delete(self, request, *args, **kwargs):
    if request.method == 'DELETE':
      pk = kwargs.get('pk')

      try:
        blog = Blog.objects.get(id=pk)
      
      except Blog.DoesNotExist:
        return Response({"message":"Blog does not exist"}, status=status.HTTP_404_NOT_FOUND)

      blog.delete()

      return Response({"message":"blog deleted"}, status= status.HTTP_200_OK)






    
