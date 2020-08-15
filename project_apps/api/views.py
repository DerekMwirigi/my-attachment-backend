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

class SignUp_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        valid = True
        errors = []
        response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': request.data }
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def post(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Account Not created', 'data': None }
        try:
            user = User(
                username=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                phone=request.data['phone'],
                email=request.data['email'],
                user_role=int(request.data['user_role'])
            )
            user.set_password(request.data['password'])
            user.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Account created', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

class SignIn_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        valid = True
        errors = []
        response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': request.data }
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def post(self, request, format=None):
        valid = True
        errors = []
        response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': request.data }
        return HttpResponse(json.dumps(response), content_type='application/json') 

class StudentLogBook_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        valid = True
        errors = []
        try:
            
            response = { 'status': True, 'status_code': 1, 'status_message': 'Success', 'errors': errors, 'message': 'Here is the data', 'data': data }
        except Exception as inst:
            errors =str(inst)
            response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': '' }
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def post(self, request, format=None):
        valid = True
        errors = []
        try:
            response = { 'status': True, 'status_code': 1, 'status_message': 'Success', 'message': 'Done', 'data': request.data['id'] }
        except Exception as inst:
            errors =str(inst)
            response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': None }
        return HttpResponse(json.dumps(response), content_type='application/json') 
        

class LecturerStudentAssingment_APS(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        valid = True
        errors = []
        try:
            
            response = { 'status': True, 'status_code': 1, 'status_message': 'Success', 'errors': errors, 'message': 'Here is the data', 'data': data }
        except Exception as inst:
            errors =str(inst)
            response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': '' }
        return HttpResponse(json.dumps(response), content_type='application/json') 
