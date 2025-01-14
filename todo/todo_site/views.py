from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TodoForm
from .models import Todo

def index(request):
    item_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
    context = {
        'forms': form,
        'list': item_list,
        'title': 'Список задач'
    }
    return render(request, 'todo_site/index.html', context)

def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Задача удалена!')
    return redirect('todo')