from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm


# Create your views here.
def task_index(request):
    tasks = Task.objects.filter(complete=False)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_index')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_index.html', {'tasks': tasks, 'form': form})


@login_required
def update_task(request, pk):
    task = Task.objects.get(pk=pk)

    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid() and task.complete:
            form.save()
            return redirect('done_task')
        elif form.is_valid():
            form.save()
            return redirect('task_index')

    return render(request, 'tasks/task_update.html', {'form': form})


@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method == 'POST':
        task.delete()
        return redirect('done_task')

    return render(request, 'tasks/task_delete.html', {'task': task})


def done_task(request):
    tasks = Task.objects.filter(complete=True, )
    return render(request, 'tasks/task_done.html', {'tasks': tasks})
