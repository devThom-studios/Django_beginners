from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_id']
    pass
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name']
    pass