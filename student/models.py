from django.db import models
class Student(models.Model):
    stufname = models.CharField(max_length=100, unique=True)
    stulname = models.CharField(max_length=100, unique=True)
    stuemail = models.EmailField(unique=True)
    stupassword = models.CharField(max_length=100)
    stumobile = models.CharField(max_length=100)
    def __str__(self):
        return self.stufname