from .models import User
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import facebook
from rest_framework.authtoken.models import Token
import json

#mexendo com html _> daqui pra baixo
from django.shortcuts import render
from django.http import HttpResponse


def privacypolicy(request):
 return render(request, 'core/index.html')
 # <- daqui pra cima mexendo html
