import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'projectX6_orm.settings')
import django
django.setup()

from app.models import *
from faker import Faker
from random import *
fake=Faker()

def populate(n):
    for i in range(n):
        fname=fake.name()
        fcity=fake.city()
        fno=randint(1,200)
        fsal=randint(10000,80000)
        employee.objects.get_or_create(ename=fname,ecity=fcity,esal=fsal,eno=fno)

populate(25)
