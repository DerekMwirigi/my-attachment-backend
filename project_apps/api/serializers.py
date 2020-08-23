from rest_framework import serializers
from .models import User, StudentLogBook, StudentLogBookItem, StudentAttachmentLocation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'phone', 'email', 'user_role')

class StudentLogBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLogBookItem
        fields = ('id','date', 'worked_on', 'created_on', 'status')

class StudentLogBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLogBook
        fields = ('id','label', 'created_on', 'status')

class StudentAttachmentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttachmentLocation
        fields = ('id', 'street', 'lat', 'lng', 'info')
