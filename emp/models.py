from django.db import models


class Firma(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Employee(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    nid = models.CharField(max_length=255)
    number = models.CharField(max_length=255)


class Income(models.Model):
    vorname = models.CharField(max_length=255)
    nachname = models.CharField(max_length=255)
    day = models.CharField(max_length=255)
    monat = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)