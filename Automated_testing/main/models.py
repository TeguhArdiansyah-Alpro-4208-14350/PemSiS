from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def is_member(self, user):
        return self.members.filter(user=user).exists()

class CourseMember(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
