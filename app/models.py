from django.db import models
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 100)
    reg_no = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.reg_no
    