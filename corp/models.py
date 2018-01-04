from django.db import models
from django.forms import ModelForm



class Corps(models.Model):
    title = models.CharField(max_length=256)
    industry = models.ForeignKey('Company_Idustry', related_name='Company_Idustry', on_delete = models.CASCADE,)
    company_land = models.ForeignKey('Company_land', related_name='Company_land', on_delete = models.CASCADE,)
    cashflow = models.ForeignKey('Cashflow', related_name='Cashflow', on_delete = models.CASCADE,)
    number_of_employees = models.ForeignKey(
        'Number_of_employees', 
        related_name='Number_of_employees', 
        on_delete = models.CASCADE,
    )

#    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Company_Idustry(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title


class Company_land(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Cashflow(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class Number_of_employees(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

