from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

from random import randint

def index(request):
    return render(request, 'home.html')


def CountFibonacci():
    first_number = 1
    second_number = 1
    return_list = [first_number, second_number]

    for i in range(10):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
        return_list.append(third_number)
    return str(return_list)[1:-1]


def CountFibonacciList():
    first_number = 1
    second_number = 1
    return_list = [first_number, second_number]

    for i in range(10):
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number
        return_list.append(third_number)
    return return_list


class ExampleClassBased(View):
    def get(self, request):
        return HttpResponse(f"""
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">
            </head>
            Hello, example class based world!
            <br>
            Also, here's a Fibonacci sequence for ya folks out there: {CountFibonacci()}
            <br>
            <a href="/">На главную страницу</a>
            """)


class ExampleStaticClassBased(View):
    def get(self, request):
        return render(request, 'example.html')


class ExampleTemplatedView(View):
    def get(self, request):
        return render(request, 'templated_example.html', { 'some_variable' : str(randint(0, 100))})


class ExampleTemplatedViewWithTags(View):
    def get(self, request):
        return render(request, 'templated_example_with_tags.html', {'list' : CountFibonacciList()})


class ExampleTempledViewWithInheritance(View):
    def get(self, request):
        return render(request, 'child_page.html', {'elements' : [randint(1,100) for i in range(10)]})



class ExampleTempledSecondViewWithInheritance(View):
    def get(self, request):
        return render(request, 'second_child_page.html', {'elements' : [i for i in range(10)]})
