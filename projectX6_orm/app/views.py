from django.shortcuts import render
from app.models import employee
from django.db.models.functions import Lower


# Create your views here.
def display(request):
    e1=employee.ab.get_queryset('-esal')
    #e1=employee.ab.get_emp_range(10000,20000)
    #e1=employee.ab.get_emp_sorted('ename')
    dict={'e1':e1}
    return render(request,"app/list.html",context=dict)
