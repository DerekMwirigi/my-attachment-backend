from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core import serializers
from django.contrib.auth.models import User
from . import tasks
import json
from django.http import HttpResponse
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from rest_framework.decorators import api_view, permission_classes
from .models import (
    Course,
    Student, 
    Lecturer,
    LecturerStudentAssignment,
    StudentLogBookItem,
    StudentLogBook,
    StudentAttachmentLocation
)

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
            logbook = StudentLogBook.objects.filter(id=request.GET['logbook_id']).first()
            student = Student.objects.filter(id=logbook.student.id).first()
            logbook_items = StudentLogBookItem.objects.filter(logbook=logbook)
            logbook_items_ = []
            for logbookitem in logbook_items:
                logbook_items_.append({
                    'worked_on': logbookitem.worked_on,
                    'status':logbookitem.status,
                    'date':str(logbookitem.date),
                })
            data = {
                'label':logbook.label,
                'code':logbook.code.hex,
                'status':logbook.status,
                'student':{
                    'id':student.id,
                    'names':student.names,
                    'email':student.email,
                    'phone':student.phone,
                    'regno':student.regno,
                    'course':student.course.name
                },
                
                'logbook_items': logbook_items_
            }
            response = { 'status': True, 'status_code': 1, 'status_message': 'Success', 'errors': errors, 'message': 'Here is the data', 'data': data }
        except Exception as inst:
            errors =str(inst)
            response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': '' }
        return HttpResponse(json.dumps(response), content_type='application/json') 

    def post(self, request, format=None):
        valid = True
        errors = []
        response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': request.data }
        return HttpResponse(json.dumps(response), content_type='application/json') 

class LecturerStudentAssingment_APS(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        valid = True
        errors = []
        try:
            lecturer = Lecturer.objects.filter(id=request.GET['lecturer_id']).first()
            assignments = LecturerStudentAssignment.objects.filter(lecturer=lecturer)
            students_ = []
            for assignment in assignments:
                student = Student.objects.filter(id=assignment.student.id).first()
                attachment_location = StudentAttachmentLocation.objects.filter(student=student).first()
                students_.append({
                    'id':student.id,
                    'names':student.names,
                    'email':student.email,
                    'phone':student.phone,
                    'regno':student.regno,
                    'course':student.course.name,
                    'attachment_location': {
                        'street': attachment_location.street,
                        'lat': attachment_location.lat,
                        'lng': attachment_location.lng,
                        'info':attachment_location.info
                    }
                })
            data = {
                'names':lecturer.names,
                'email':lecturer.email,
                'phone':lecturer.phone,
                'students': students_
            }
            response = { 'status': True, 'status_code': 1, 'status_message': 'Success', 'errors': errors, 'message': 'Here is the data', 'data': data }
        except Exception as inst:
            errors =str(inst)
            response = { 'status': False, 'status_code': 0, 'status_message': 'Failed', 'errors': errors, 'message': 'Sorry, there were some errors', 'data': '' }
        return HttpResponse(json.dumps(response), content_type='application/json') 
