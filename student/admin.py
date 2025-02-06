from django.contrib import admin
from student.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('stufname', 'stulname','stuemail','stupassword','stumobile')
