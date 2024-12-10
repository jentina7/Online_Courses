from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='users_list')
router.register(r'category', CategoryViewSet, basename='category_list')
router.register(r'certificate', CertificateViewSet, basename='certificate_list')
router.register(r'review', ReviewViewSet, basename='review_list')

urlpatterns = [
    path('', include(router.urls)),
    path("course/", CourseListViewSet.as_view(), name= "course_list"),
    path("course/<int:pk>", CourseDetailMixins.as_view(), name= "course_detail"),

    path("exam/", ExamListViewSet.as_view(), name= "exam_list"),
    path("exam/<int:pk>", ExamDetailMixins.as_view(), name= "exam_detail"),
]