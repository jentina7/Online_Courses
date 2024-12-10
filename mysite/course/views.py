from rest_framework import viewsets, generics, permissions
from .serializers import *
from .models import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class UserProfileCourseViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileCourseSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category_name']
    search_fields = ['category_name']


class CourseListViewSet(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializers


class CourseDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializers


class LessonListViewSet(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializers


class LessonDetailMixins(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializers


class AssignmentListViewSet(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializers


class AssignmentDetailMixins(generics.RetrieveDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializers


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers


class ExamListViewSet(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers


class ExamDetailMixins(generics.RetrieveDestroyAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializers


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer