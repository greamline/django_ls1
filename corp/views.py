from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import JsonResponse
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from . import models
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import Corp_Form


# Create your views here.



class CorpsListView(ListView):
    model = models.Corps
               
#def main(request):
#    models = corp.company_land
#   return render(request, 'corp.html')


def get_corp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Corp_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            #form = form.full_clean()
            #print(form)
            form = form.cleaned_data
            #print(form)
            #form = form.cleaned_data('title', 'industrу', 'company_land', 'cashflow', 'number_of_employees')
            #f = form(corp_name, Company_Idustry, company_land, )
            # ...
            # redirect to a new URL:
            print(form)
            #new_company = form.save_m2m()
            temp_data = form.save
            print(temp_data)
           
            return HttpResponseRedirect('/c')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Corp_Form()

    return render(request, 'corp.html', {'form': form})