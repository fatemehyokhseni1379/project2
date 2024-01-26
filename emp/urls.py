from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-office", views.addOffice, name="addOffice"),
    path("save-office", views.saveOffice, name="saveOffice"),
    path("offices", views.offices, name="offices"),
    path("add-emp", views.addEmp, name="addEmp"),
    path("save-emp", views.saveEmp, name="saveEmp"),
    path("emps", views.emps, name="emps"),
    path("add-income", views.addIncome, name="addIncome"),
    path("save-income", views.saveIncome, name="saveIncome"),
]