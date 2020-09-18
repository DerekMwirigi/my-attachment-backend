from rest_framework.parsers import JSONParser
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny, IsAuthenticated
)
from .tasks import AfricasTalking
import json
from django.http import HttpResponse

# Create your views here.

class ExpressSMS(APIView):
    parser_classes = [JSONParser]
    permission_classes = [AllowAny]
    
    def get(self, request, format=None):
        return HttpResponse(json.dumps(request.data), content_type='application/json')           

    def post(self, request, format=None):
        message = {
            'text': request.data['text'],
            'recipients': request.data['recipients']
        }
        response = AfricasTalking(request.data['api_key'], request.data['user_name']).direct_send(message)
        
        return HttpResponse(json.dumps(response), content_type='application/json')           
