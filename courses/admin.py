from django.contrib import admin
from .models import Courses
from django import forms
from category.models import Category
class CourseForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course_cat'].widget.choices = [(cat.id, cat.categoryName) for cat in Category.objects.all()]
#@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    form=CourseForm
    list_display = ('courseName', 'courseFees','categoryName','courseDuration','created_at')
    def categoryName(self, obj): # to show the cat_name from category model
        return obj.course_cat.categoryName
admin.site.register(Courses, CourseAdmin)