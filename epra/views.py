import datetime

from django.db.models import F, IntegerField
from django.db.models.functions import Cast, ExtractDay
from django.shortcuts import render
from django.views import generic
from .models import Project, Employee
# Create your views here.

def fill_peroid(month):
    period = []
    start = datetime.datetime(2021, month, 10)
    end = start + datetime.timedelta(days=30)
    end = end - datetime.timedelta(days=1)
    p = start
    while True:
        period.append(p)
        p = p + datetime.timedelta(days=1)
        if p >= end:
            break
    return period

class Dashbord(generic.ListView):
    model = Employee
    queryset = Employee.objects.all()
    template_name = "epra/index.html"


    def get_queryset(self):
        res = Employee.objects.values('name', 'project__name', 'project__start', 'project__end').annotate(
            pr_start=ExtractDay(F('project__start')),
            pr_end=ExtractDay(F('project__end'))
        )
        return res

    def get_context_data(self, **kwargs):
        context = super(Dashbord, self).get_context_data(**kwargs)
        context['period'] = fill_peroid(11)
        return context