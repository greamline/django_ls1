from django import forms
from .models import Corps, Company_Idustry, Company_land, Cashflow, Number_of_employees


class Corp_Form(forms.Form):
	title = forms.CharField(label='Название компании', max_length=50)
	industry = forms.ModelMultipleChoiceField(label='Род деятельности', queryset=Company_Idustry.objects.all())
	company_land = forms.ModelMultipleChoiceField(label='Штаб квартира', queryset=Company_land.objects.all())
	cashflow = forms.ModelMultipleChoiceField(label='Годовой оборот', queryset=Cashflow.objects.all())
	number_of_employees = forms.ModelMultipleChoiceField(label='Количество сотрудников', queryset=Number_of_employees.objects.all())