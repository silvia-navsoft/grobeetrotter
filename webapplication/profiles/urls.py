from django.urls import path, include
from .views import *

urlpatterns = [
  path('superadmin/login',SuperAdminLoginView.as_view(), name="admin login")
    ]