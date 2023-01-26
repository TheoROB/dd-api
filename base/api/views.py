from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse

from base.models import Player


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         token['username'] = user.username
#         # ...

#         return token


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        # '/api/token',
        # '/api/token/refresh',
        '/api/students',
        '/api/students/id',
        '/api/students/popularity'
    ]

    return Response(routes)

def allStudents(request):
    students = Player.objects.all()
    return HttpResponse(students)

def studentID(request):
    return HttpResponse("ID de l'étudiant")

def orderStudentsByPopularity(request):
    return HttpResponse("Classement des 2tudiants par popularité")