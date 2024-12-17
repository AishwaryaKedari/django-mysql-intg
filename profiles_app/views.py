from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
# from rest_framework import filters
# from rest_framework import viewsets
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.settings import api_settings
# from rest_framework.permissions import IsAuthenticated

# from profiles_app import serializers
# from profiles_app import models
# from profiles_app import permission
# # Create your views here.



# class UserProfileViewSet(viewsets.ModelViewSet):
#     """creating updating profiles"""
#     serializer_class = serializers.UserProfileSerializer
#     queryset = models.UserProfile.objects.all()
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (permission.UpdateOwnProfile,)
#     filter_backends = (filters.SearchFilter,)
#     search_fields = ('name', 'email',)
