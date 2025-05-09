from django.shortcuts import render, redirect, get_object_or_404
from .models import Bottle
from .forms import BottleForm, CalculateRemainingForm

# Представление для отображения всех бутылок
def bottle_list(request):
    bottles = Bottle.objects.all()
    return render(request, 'main/bottle_list.html', {'bottles': bottles})

# Представление для создания новой бутылки
def bottle_create(request):
    if request.method == 'POST':
        form = BottleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bottle_list')
    else:
        form = BottleForm()
    return render(request, 'main/bottle_form.html', {'form': form})

# Представление для редактирования бутылки
def bottle_edit(request, pk):
    bottle = get_object_or_404(Bottle, id=pk)
    if request.method == 'POST':
        form = BottleForm(request.POST, instance=bottle)
        if form.is_valid():
            form.save()
            return redirect('bottle_list')
    else:
        form = BottleForm(instance=bottle)
    return render(request, 'main/bottle_form.html', {'form': form})

# Представление для удаления бутылки
def bottle_delete(request, pk):
    bottle = get_object_or_404(Bottle, pk=pk)
    if request.method == 'POST':
        bottle.delete()
        return redirect('bottle_list')
    return render(request, 'main/bottle_confirm_delete.html', {'bottle': bottle})

# Представление для расчёта оставшегося объёма бутылки
def calculate_remaining(request, bottle_id):
    bottle = get_object_or_404(Bottle, id=bottle_id)
    remaining_volume = None

    if request.method == 'POST':
        form = CalculateRemainingForm(request.POST)
        if form.is_valid():
            current_weight = form.cleaned_data['current_weight']
            remaining_volume = bottle.calculate_remaining_volume(current_weight)
    else:
        form = CalculateRemainingForm()

    return render(request, 'main/calculate_remaining.html', {
        'form': form,
        'bottle': bottle,
        'remaining_volume': remaining_volume,
    })