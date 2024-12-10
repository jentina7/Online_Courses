from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users_list')
router.register(r'category', CategoryViewSet, basename='category_list')
router.register(r'certificate', CertificateViewSet, basename='certificate_list')
router.register(r'review', ReviewViewSet, basename='review_list')
router.register(r'assignment', AssignmentViewSet, basename='assignment_list')


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('', include(router.urls)),
    path("course/", CourseListViewSet.as_view(), name= "course_list"),
    path("course/<int:pk>", CourseDetailViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update', 'delete': 'destroy'}), name= "course_detail"),

    path("exam/", ExamListViewSet.as_view(), name= "exam_list"),
    path("exam/<int:pk>", ExamDetailMixins.as_view(), name= "exam_detail"),
]