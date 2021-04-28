from rest_framework.views import APIView
from rest_framework.response import Response
from ..profiles.serializers import *
from ..profiles.models import *
import jwt
import datetime

class CollegeListView(APIView):
    def get(self, request):
        college_list=User.objects.filter(user_type=4,user_status="Yes")
        college_serializer=UserSerializer(college_list, many=True)
        output=college_serializer.data
        columns=[
        'select',
        'college_name',
       'representative_name',
       'representative_email',
       'representative_phone',
       'representative_status',
       'action'
    ],
        for element in output:
            element["representative_name"]=element["user_fname"]+" "+element["user_lname"]
            user_college=EducationalDetails.objects.get(user_id=element["user_id"],edu_details_status="Yes")
            element["college_name"]=user_college.college_name
            element["edit"]="fa fa-pencil"
            element["delete"]="fa fa-trash-o"
        return Response({"status":200, "columns":columns,"data":output})



