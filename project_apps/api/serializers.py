from rest_framework import serializers
from .models import StudentLogBook, StudentLogBookItem

class StudentLogBookItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLogBookItem
        fields = ('id','date', 'worked_on', 'created_on', 'status')

class StudentLogBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLogBook
        fields = ('id','label', 'created_on')

