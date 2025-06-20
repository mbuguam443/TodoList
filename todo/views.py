# todo/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo/index.html', {'tasks': tasks, 'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('index')