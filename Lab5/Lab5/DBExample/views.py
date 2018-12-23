from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Programmer, Project, Program

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


def getSubjectAreaInfo():

    programmers = []
    for programmer in Programmer.objects.all():
        programmerinfo = {}
        programmerinfo['firstname'] = programmer.first_name
        programmerinfo['username'] = programmer.username
        programmerinfo['lastname'] = programmer.last_name
        programmerinfo['programs'] = []
        for program in Program.objects.filter(programmers=programmer):
            programmerinfo['programs'].append(program.programName)
        programmers.append(programmerinfo)

    subjectAreaDict = {'programmers' : programmers}
    return subjectAreaDict

class ModelView(View):
    def get(self, request):
        return render(request, 'myModels.html', getSubjectAreaInfo())

class AddProgram(View):
    def get(self, request):
        #a = Programmer.objects.get(username='pipoper')
        #p = Program(programName='Stendhack', description='Набор инструментов для реверс-инжиниринга эмулятора Stend.exe')
        #p.save()
        #p.programmers.add(a)
        #p = Program.objects.get(programName='Storyboard VN')
        return render(request, 'myModels.html', getSubjectAreaInfo())
