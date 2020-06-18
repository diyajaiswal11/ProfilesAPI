from rest_framework import serializers
from .models import UserProfile, Favourite

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=UserProfile
        fields=['firstname','lastname','email','password']

        """def restore_object(self, attrs, instance=None):
            attrs['password'] = make_password(attrs['password'])
            return super(UserProfileSerializer, self).restore_object(attrs, instance=None)
        """


class FavouriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ('userid', 'category')

class FavouriteSerializer1(serializers.ModelSerializer):

    class Meta:
        model = Favourite
        fields = ['category']
