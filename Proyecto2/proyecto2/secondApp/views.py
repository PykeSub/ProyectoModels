from django.shortcuts import render
from secondApp.models import Employee
# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados' : empleados}
    return render (request, 'empleados.html', data)