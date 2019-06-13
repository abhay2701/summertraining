from django.db import models

# Create your models here.
class custommanager(models.Manager):
    def get_queryset(self,a):
        return super().get_queryset().order_by(a)

    def get_emp_range(self,range1,range2):
        return super().get_queryset().filter(esal__range=(range1,range2)).order_by('esal')

    def get_emp_sorted(self,param):
        return super().get_queryset().order_by(param)

class employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    ecity=models.CharField(max_length=30)
    ab=custommanager()
