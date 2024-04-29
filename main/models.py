from django.db import models

# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=255)
    menu_id = models.IntegerField()
    parent_id = models.IntegerField()

class Degree(models.Model):
    degree_id = models.IntegerField(null=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prerequsites = models.CharField(max_length=512)
    parent_id = models.IntegerField()


class Program(models.Model):
    program_id = models.IntegerField(null=False)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, to_field='degree_id')

class Info(models.Model):
    program_id = models.IntegerField()
    parent_id = models.IntegerField()
    content = models.CharField(max_length=1200)
    ref_to_site = models.CharField(max_length=255)


class Admission(models.Model):
    regular = models.CharField(max_length=255)
    accelerated = models.CharField(max_length=255)
    parent_id = models.IntegerField()