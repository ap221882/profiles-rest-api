from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
 def get(self,request,format=None):
  """Returns a list of APIView features"""
  an_apiview=[
   'Uses HTTP methods as function (get, post, patch, put, patch)',
   'Is similar to a traditional Django view',
   'Gives you most control',
   'Is mapped manually to urls'
  ]

  return Response({'message':'Hello', 'an_apiview':an_apiview})