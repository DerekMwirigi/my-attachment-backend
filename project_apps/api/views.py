from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from . import tasks
import json
from django.http import HttpResponse
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from rest_framework.decorators import api_view, permission_classes

from .models import (
    User,
    Course,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)

from .serializers import StudentLogBookSerializer, StudentLogBookItemSerializer

class SignUp_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Account Not created', 'data': None }
        try:
            obj = User(
                username=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                phone=request.data['phone'],
                email=request.data['email'],
                user_role=int(request.data['user_role'])
            )
            obj.set_password(request.data['password'])
            obj.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Account created', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

class StudentLogBook_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'No items', 'data': None }
        try:
            logbook = StudentLogBook.objects.get(student=request.user)
            data = StudentLogBookSerializer(logbook, many=False).data
            logbook_items = StudentLogBookItem.objects.filter(logbook=logbook)
            data['items'] = StudentLogBookItemSerializer(logbook_items, many=True).data
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Items', 'data': data }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 
    
class StudentLogBookItem_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
   
    def post(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            obj = StudentLogBookItem(
                date = request.data['date'],
                worked_on = request.data['worked_on'],
                logbook = StudentLogBook.objects.get(student=request.user)
            )
            obj.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Saved', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def put(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            obj = StudentLogBookItem.objects.get(id=int(request.data['date']))
            obj.worked_on = request.data['worked_on']
            obj.status = int(request.data['status'])
            obj.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Saved', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 