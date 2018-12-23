from django.db import models


class Programmer(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True, blank=True, null=True)
    telephone = models.CharField(max_length=12, unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField(null=True, blank=True)
    sex = models.CharField(max_length=1, default='M')


class Program(models.Model):
    programName = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    programmers = models.ManyToManyField(Programmer)


class Site(models.Model):
    url = models.CharField(max_length=255, unique=True)
    siteName = models.CharField(max_length=255, blank=True)
    programmers = models.ManyToManyField(Programmer)


class Screenshot(models.Model):
    filename = models.CharField(max_length=255)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Techfield(models.Model):
    naming = models.CharField(max_length=255)


class Project(models.Model):
    projectName = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    techfield = models.ForeignKey(Techfield, on_delete=models.CASCADE)
    programs = models.ManyToManyField(Program)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)


class Milestone(models.Model):
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
