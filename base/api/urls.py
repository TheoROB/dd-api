from django.urls import path
from . import views
# from .views import MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

urlpatterns = [
    path('', views.getRoutes),
    path('students/', views.allStudents),
    path('student/id/', views.studentID),
    path('students/popularity', views.orderStudentsByPopularity,)

    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]