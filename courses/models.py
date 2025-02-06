from django.db import models
from category.models import Category
from tinymce.models import HTMLField
class Courses(models.Model):
    courseName = models.CharField(max_length=200)
    courseFees = models.CharField(max_length=200)
    courseDuration = models.CharField(max_length=200)
    courseDescription = HTMLField()
    courseImage = models.ImageField(upload_to='course_image/')
    course_cat=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(auto_now_add=True)  
  
def __str__(self):
        return self.courseName  
