from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("username", "email", "password", "first_name", "last_name", "age",
                  "bio", "phone_number", "profile_picture", "user_role")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            "user": {
                "username": instance.username,
                "email": instance.email,
            },
            'access': str(refresh.access_token),
            "refresh": str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only= True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")


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


class CourseExamSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    class Meta:
        model = Course
        fields = ['course_name', 'category']


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
    course = CourseExamSerializers()
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


class CourseDetailSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    created_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    updated_at = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    created_by = UserProfileCourseSerializers()
    lesson_course = LessonDetailSerializers(read_only=True, many=True)
    questions = QuestionSerializers(read_only=True, many=True)
    class Meta:
        model = Course
        fields = ['category', 'course_name', 'description', 'level', 'price', 'created_by', 'created_at', 'updated_at', 'lesson_course', 'questions']

