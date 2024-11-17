from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task
from .forms import TaskForm

@login_required
def todolist(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user 
            task.save()
            return redirect('taskslist')
    else:
        form = TaskForm()
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo_app/todoapp.html', {'form':form, 'tasks': tasks})
    

@login_required
def task_update(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskslist')
    else:
        form = TaskForm(instance=task)
        tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo_app/todoapp.html', {'form': form, 'tasks':tasks})

@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('taskslist')

@login_required
def task_toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if task.status == 'P':
        task.status = 'C'
    else:
        task.status = 'P'
    task.save()
    return redirect('taskslist')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def custom_404(request, exception):
    return render(request, '404.html', status=404)