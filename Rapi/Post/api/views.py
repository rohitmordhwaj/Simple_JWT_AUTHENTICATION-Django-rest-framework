from rest_framework.views  import APIView
from rest_framework import generics

from rest_framework.response import Response 
from Post.models import Post,Author
from .serializers import PostSerializer




class  StudentAPIView(generics.ListAPIView):
	#permission_classes 		= []
	#authentication_classes 	= []
	queryset                = Post.objects.all()
	serializer_class        = PostSerializer




class  StudentCreateAPIView(generics.CreateAPIView):
	#permission_classes 		= []
	#authentication_classes 	= []
	queryset                = Post.objects.all()
	serializer_class        = PostSerializer






