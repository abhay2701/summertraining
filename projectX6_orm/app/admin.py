from django.contrib import admin
from app.models import employee

# Register your models here.
class employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','ecity']

admin.site.register(employee,employeeadmin)    
