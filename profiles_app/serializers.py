# from rest_framework import serializers
# from profiles_app import models

# class UserProfileSerializer(serializers.ModelSerializer):
#     """Serializes a user profile object"""

#     class Meta:
#         model = models.UserProfile
#         fields = ('id', 'email', 'name', 'password')
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'style': {'input_type': 'password'}
#             }
#         }

#     def create(self, validated_data):
#         """Create and return a new user"""
#         user = models.UserProfile.objects.create_user(
#             email=validated_data['email'],
#             name=validated_data['name'],
#             password=validated_data['password']
#         )

#         return user
    
# class UserProfile(AbstractBaseUser, PermissionsMixin):
#     """Database model for users in the system"""
#     email = models.EmailField(max_length=255, unique=True)
#     name = models.CharField(max_length=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = UserProfileManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         """Retrieve full name for user"""
#         return self.name

#     def get_short_name(self):
#         """Retrieve short name of user"""
#         return self.name

#     def __str__(self):
#         """Return string representation of user"""
#         return self.email
