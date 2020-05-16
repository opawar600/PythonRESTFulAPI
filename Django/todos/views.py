from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Todo

# Create your views here.
def todos(request):
    todos_list = Todo.objects.all()
    data = {
        "todos": list(todos_list.values(
            "todo", "done"
        ))
    }
    return JsonResponse(data)

def single_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    data = {
        "todo": todo.todo,
        "done": todo.done
    }
    return JsonResponse(data)
