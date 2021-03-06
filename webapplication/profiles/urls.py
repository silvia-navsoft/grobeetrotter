from django.urls import path, include
from .views import *
from ..admin_view.views import *
urlpatterns = [
  path('superadmin/login',SuperAdminLoginView.as_view(), name="admin login"),
  path('college/list',CollegeListView.as_view(), name="admin login"),
  path('forgotpassword/',ForgotPassSendMail.as_view(), name="admin login"),
  path('receive/forgot/code',ReceiveForgotCode.as_view(), name="receive code"),
  path('change/forgot/pass',ChangePassForgot.as_view(), name="change password"),
    ]