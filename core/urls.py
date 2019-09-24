from django.urls import path
from . import views

urlpatterns = [
    path('privacypolicy/',views.privacypolicy, name="privacypolicy"),
    path('login/', views.login_view, name='login'),
]
