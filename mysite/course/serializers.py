from rest_framework import serializers
from .models import *


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']


class CourseListSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = Course
        fields = ['course_name', 'category', 'price']


class CourseDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    created_by = UserProfileCourseSerializers()
    class Meta:
        model = Course
        fields = '__all__'


class LessonListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'course']


class LessonDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'video_url', 'course']


class AssignmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'student']


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['questions']


class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['title', 'course', 'questions', 'passing_score', 'duration']


class CertificateSerializers(serializers.ModelSerializer):
    issued_at = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Certificate
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    class Meta:
        model = Review
        fields = ['user', 'course', 'comment', 'rating', 'created_date']


