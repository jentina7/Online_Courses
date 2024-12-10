from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(default=0)
    phone_number = models.CharField(max_length=20, unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to="profile_images/")
    ROLE_CHOICES = (
        ('клиент', 'клиент'),
        ('преподаватель', 'преподаватель')
    )
    user_role = models.CharField(max_length=16, choices=ROLE_CHOICES, default='клиент')

    def __str__(self):
        return self.first_name or self.username


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    LEVEL_CHOICES = (
        ('начальный', 'начальный'),
        ('средний', 'средний'),
        ('продвинутый', 'продвинутый')
    )
    level = models.CharField(max_length=16, choices=LEVEL_CHOICES, default='начальный')
    price = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='created_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.category} - {self.created_by} - {self.course_name}'


class Lesson(models.Model):
    title = models.CharField(max_length=64)
    video_url = models.FileField(upload_to="lesson_video/")
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.course} - {self.student}'


class Question(models.Model):
    questions = models.FileField(upload_to="questions/")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return self.questions.name


class Exam(models.Model):
    title = models.CharField(max_length=64)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    questions = models.ManyToManyField(Question)
    passing_score = models.PositiveSmallIntegerField(default=0)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title} - {self.course}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(upload_to="certificate_url/")

    def __str__(self):
        return f"{self.course} - {self.student}"


class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_reviews")
    comment = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.course}"
