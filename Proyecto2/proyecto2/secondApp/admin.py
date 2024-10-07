from django.contrib import admin
from secondApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fono']

# Register your models here.
admin.site.register(Employee, EmployeeAdmin)