#mexendo com html _> daqui pra baixo
from django.shortcuts import render
from django.http import HttpResponse

#upload image imports
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status, generics

from core.serializers import FileSerializer
from core.models import User


def privacypolicy(request):
 return render(request, 'core/index.html')
 # <- daqui pra cima mexendo html



class uploadProfilePic(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
 #upload user profile_image
    #parser_classes = (JSONParser, MultiPartParser, FormParser,)
    queryset = User.objects.all()
    serializer_class = FileSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
