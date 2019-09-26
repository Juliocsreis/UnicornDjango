from django.urls import path
from . import views


urlpatterns = [
    path('privacypolicy/', views.privacypolicy, name="privacypolicy"),
    path('upload/', views.uploadProfilePic.as_view(), name='uploadProfilePic'),
]
