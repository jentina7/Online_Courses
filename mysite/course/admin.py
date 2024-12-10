from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationInlineModelAdmin
from .models import *


class LessonInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Lesson
    extra = 1


class AssignmentInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Assignment
    extra = 1


class QuestionInline(TranslationInlineModelAdmin, admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    inlines = [LessonInline, AssignmentInline, QuestionInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Category)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(Exam)
admin.site.register(Certificate)
admin.site.register(Review)
