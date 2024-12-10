from rest_framework import permissions
from rest_framework.permissions import BasePermission


class CheckCRUD(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user


class CheckPostPut(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['POST', 'PUT', 'PATCH']:
            return request.user.is_authenticated and request.user.user_role == 'преподаватель'
        return request.user.is_authenticated


class CheckReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.course.created_by:
            return True
        return False


class ViewCourses(permissions.BasePermission):
    def has_permission(self, request, view):
        return True


class CheckExam(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.student_exam.user_role=="клиент"


class StudentReview(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.student_exam.user_role=="клиент"


class GetCertificate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.student_exam.user_role=="клиент"