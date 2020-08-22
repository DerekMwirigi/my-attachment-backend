from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from . import tasks

from config.utils import date_filter_split

import json
import requests

from django.http import HttpResponse
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)

from rest_framework_simplejwt import views as jwt_views

from rest_framework.decorators import api_view, permission_classes

from .models import (
    User,
    Course,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)

from .serializers import UserSerializer, StudentLogBookSerializer, StudentLogBookItemSerializer, StudentAttachmentLocationSerializer

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
            # create default logbook
            if int(request.data['user_role']) == 2:
                logbook = StudentLogBook(
                    student=obj
                )
                logbook.save()
            # create access (token)
            payload = {'username':request.data['email'], 'password': request.data['password']}
            http_response = requests.post(url='http://138.197.196.78/api/sign-in/', json=payload)
            if http_response.status_code == 200:
                response = json.loads(http_response.content)
            else:
                response['errors'].append('Created but NOT signed In')
                obj.delete()
                logbook.delete()
        except Exception as ex:
            response['errors'].append(str(ex))
        return HttpResponse(json.dumps(response), content_type='application/json') 

class Account_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Account', 'data': None }
        try:
            data = UserSerializer(request.user, many=False).data
            if request.user.user_role == 2:
                data['address'] = StudentAttachmentLocationSerializer(StudentAttachmentLocation.objects.get(student=request.user), many=False).data
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Account', 'data': data }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

class StudentLogBook_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'No items', 'data': None }
        try:
            if request.user.user_role == 1:
                student = User.objects.get(pk=int(request.GET['student_id']))
                logbook = StudentLogBook.objects.get(student=student)
            elif request.user.user_role == 2:
                logbook = StudentLogBook.objects.get(student=request.user)
            data = StudentLogBookSerializer(logbook, many=False).data
            logbook_items = StudentLogBookItem.objects.filter(logbook=logbook)
            data['items'] = StudentLogBookItemSerializer(logbook_items, many=True).data
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Items', 'data': data }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 
    
    def put(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            obj = StudentLogBook.objects.get(id=int(request.data['id']))
            obj.status = int(request.data['status'])
            obj.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Saved', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 
    
class StudentLogBookItem_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
   
    def post(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            start_date, end_date = date_filter_split(None)
            obj = StudentLogBookItem(
                date = start_date,
                worked_on = request.data['worked_on'],
                logbook = StudentLogBook.objects.get(student=request.user)
            )
            obj.save()
            logbook = StudentLogBook.objects.get(student=request.user)
            data = StudentLogBookSerializer(logbook, many=False).data
            logbook_items = StudentLogBookItem.objects.filter(logbook=logbook)
            data['items'] = StudentLogBookItemSerializer(logbook_items, many=True).data
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Items', 'data': data }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def put(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            obj = StudentLogBookItem.objects.get(id=int(request.data['id']))
            obj.worked_on = request.data['worked_on']
            obj.status = int(request.data['status'])
            obj.save()
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Saved', 'data': {} }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 

class LecturerStudentAssignment_API(APIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]
   
    def get(self, request, format=None):
        response = { 'status': False, 'status_message': 'Failed', 'errors': [], 'message': 'Not save', 'data': None }
        try:
            students = []
            lec_stds = LecturerStudentAssignment.objects.filter(lecturer=request.user)
            for lec_std in lec_stds:
                student = UserSerializer(lec_std.student, many=False).data
                student['address'] = StudentAttachmentLocationSerializer(StudentAttachmentLocation.objects.get(student=lec_std.student), many=False).data
                students.append(student)
            response = { 'status': True,  'status_message': 'Success', 'errors': [], 'message': 'Items', 'data': students }
        except Exception as ex:
            response['errors'] = [str(ex)]
        return HttpResponse(json.dumps(response), content_type='application/json') 
