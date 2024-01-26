from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Firma, Employee, Income


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def addOffice(request):
    template = loader.get_template('add-office.html')
    return HttpResponse(template.render({}, request))


def saveOffice(request):
    f = Firma(
        name = request.POST['name'],
        number = request.POST['number'],
        city = request.POST['city'],
        province = request.POST['province'],
        address = request.POST['address'],
    )
    f.save()
    return HttpResponseRedirect("/offices")


def offices(request):
    template = loader.get_template('offices.html')
    return HttpResponse(template.render({"offices": Firma.objects.all()}, request))


def addEmp(request):
    template = loader.get_template('add-emp.html')
    return HttpResponse(template.render({}, request))


def saveEmp(request):
    e = Employee(
        vorname = request.POST['vorname'],
        nachname = request.POST['nachname'],
        number = request.POST['number'],
        nid = request.POST['nid'],
    )
    e.save()
    return HttpResponseRedirect("/emps")


def emps(request):
    template = loader.get_template('emps.html')
    return HttpResponse(template.render({"emps": Employee.objects.all()}, request))


def addIncome(request):
    template = loader.get_template('add-income.html')
    return HttpResponse(template.render({}, request))


def saveIncome(request):
    i = Income(
        vorname = request.POST['vorname'],
        nachname = request.POST['nachname'],
        day = request.POST['day'],
        monat = request.POST['monat'],
        amount = request.POST['amount'],
    )
    i.save()
    return HttpResponseRedirect("/")