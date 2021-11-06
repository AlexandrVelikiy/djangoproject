from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id} {self.name} "


class Project(models.Model):
    name = models.CharField(max_length=255)
    start = models.DateField()
    end = models.DateField()
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id} {self.name} "

