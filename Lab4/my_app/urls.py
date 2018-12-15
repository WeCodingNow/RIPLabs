from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('example_class_based/', views.ExampleClassBased.as_view()),
    path('example_static/', views.ExampleStaticClassBased.as_view()),
    path('example_templated_view/', views.ExampleTemplatedView.as_view()),
    path('templated_example_with_tags/', views.ExampleTemplatedViewWithTags.as_view()),
    path('templated_example_with_inheritance/', views.ExampleTempledViewWithInheritance.as_view()),
    path('second_templated_example_with_inheritance/', views.ExampleTempledSecondViewWithInheritance.as_view()),
]
