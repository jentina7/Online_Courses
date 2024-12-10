from .models import Category, UserProfile, Course, Lesson, Assignment, Question
from modeltranslation.translator import TranslationOptions,register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', )


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('bio',)


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')


@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Question)
class LessonTranslationOptions(TranslationOptions):
    fields = ('questions',)