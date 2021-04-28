from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.validators import validate_email
from .serializers import *
import jwt
import datetime
from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.csrf import ensure_csrf_cookie

#

class SuperAdminLoginView(APIView):
    #permission_classes= [permissions.IsAuthenticated, TokenHasReadWriteScope]
    def post(self, request):
        username=request.data.get("username")
        password=request.data.get("password")
        username= username.lower()
        try:
            user=User.objects.get(username=username)
            if (user.user_password==password):
                if user.user_token is None:
                    token = jwt.encode({"user": user.user_id, "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3000)},'secret', algorithm='HS256')
                    user.user_token=token.decode('UTF-8')
                    user.save()
                user_serializer=UserSerializer(user)
                output=user_serializer.data

                return Response({"status": 200, "data":output, "message":"You are logged in"})
            else:
                return Response({"status": 401, "message":"The Password id Incorrect"})
        except:
            return Response({"status": 401, "message": "The Email Address doesn't exist"})


# class ForgotPassSendMail(APIView):
#     def post(self, request):
#         email_id=request.data.get("email")

# class CollegeAdd(APIView):
#     def post(self,request):
#         college_represent_fname=request.data.get("college_represent_fname")
#         college_represent_lname=request.data.get("college_represent_lname")
#         college_email=request.data.get("college_email")
#         college_name=request.data.get("college_name")
#         user_password=request.data.get("password")
#         try:
#          user_exists=User.objects.get(user_email=college_email)
#          if user_exists:
#              return Response({"status":status.HTTP_409_CONFLICT, "message":"The email_id is already associated"})
#         except:
#             college_save=User(user_email=college_email,user_status="Yes",user_fname=college_represent_fname,user_lname=college_represent_lname,username=college_email)
#             college_save.user_type=4
#             college_save.isSuper_admin="No"
#             college_save.isSub_admin="No"











