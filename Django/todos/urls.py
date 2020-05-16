# todos/urls.py
from django.urls import path

from .views import todos, single_todo

urlpatterns = [
    path("todos/", todos, name="todos"),
    path("todos/<int:pk>", single_todo, name="single_todo")
]
