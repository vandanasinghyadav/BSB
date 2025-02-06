from django.db import models
class Category(models.Model):
    categoryName = models.CharField(max_length=200)
    categoryDate = models.DateTimeField(auto_now_add=True)  
  
def __str__(self):
        return self.categoryName  
