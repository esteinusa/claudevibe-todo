from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localdate
from .models import Todo


@login_required
def home(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        due_date = request.POST.get('due_date') or None
        if title:
            Todo.objects.create(user=request.user, title=title, due_date=due_date)
        return redirect('home')
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'home.html', {'todos': todos, 'today': localdate()})


@login_required
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')


@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})