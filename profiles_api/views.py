# from email import message
from encodings import search_function
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models

class HelloAPIView(APIView):
 serializers_class=serializers.HelloSerializer

 def get(self,request,format=None):
  """Returns a list of APIView features"""
  an_apiview=[
   'Uses HTTP methods as function (get, post, patch, put, patch)',
   'Is similar to a traditional Django view',
   'Gives you most control',
   'Is mapped manually to urls'
  ]

  return Response({'message':'Hello', 'an_apiview':an_apiview})

 def post(self,request):
  serializer=self.serializers_class(data=request.data)

  if serializer.is_valid():
   name=serializer.validated_data.get('name')
   message=f'Hello {name}'
   return Response({'message':message})
  else:
   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 

 def put(self,request,pk=None):
  """Updating"""
  return Response({'method':'PUT'})

 def patch(self,request,pk=None):
  """PArtial Updating"""
  return Response({'method':'PATCH'})

  
 def delete(self,request,pk=None):
  """Deletion"""
  return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
 serializers_class=serializers.HelloSerializer

 def list(self,request):
  a_viewset=[1,2,3,5,7,6]
  return Response({'message':'Hello','a_viewset':a_viewset})

 def create(self,request):
  serializer = self.serializers_class(data=request.data)
  if serializer.is_valid():
   name=serializer.validated_data.get('name')
   message=f'Hello {name}'
   return Response({'message':message})
  else:
   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
 def retrieve(self,request,pk=None):
  return Response({'http_method':'GET'})

 def update(self,request,pk=None):
  return Response({'http_method':'PUT'})

 def partial_update(self,request,pk=None):
  return Response({'http_method':'PATCH'})

 def destroy(self,request,pk=None):
  return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
 serializer_class=serializers.UserProfileSerializer
 queryset=models.UserProfile.objects.all()
 authentication_classes=(TokenAuthentication,)
 permission_classes=(permissions.UpdateOwnProfile,)
 filter_backends=(filters.SearchFilter,)
 search_fields=('name','email',)

class UserLoginApiView(ObtainAuthToken):
 renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
 