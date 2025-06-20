from django.test import TestCase
from django.contrib.auth.models import User
from main.models import Course, CourseMember

class CourseModelTest(TestCase):
    def setUp(self):
        self.teacher = User.objects.create_user(username='teacher', password='123')
        self.student = User.objects.create_user(username='student', password='123')
        self.course = Course.objects.create(name="Python", teacher=self.teacher)

    def test_is_member(self):
        self.assertFalse(self.course.is_member(self.student))
        CourseMember.objects.create(course=self.course, user=self.student)
        self.assertTrue(self.course.is_member(self.student))
