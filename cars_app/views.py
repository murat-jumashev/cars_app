from django.shortcuts import render, redirect
from .forms import CarModelForm
from .models import Car

def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars_list.html', {'cars': cars})

def car_create(request):
    form = CarModelForm()
    if request.method == 'POST':
        form = CarModelForm(request.POST)
        if form.is_valid():
            new_car = form.save()
            return redirect('cars_app:car_details', pk=new_car.pk)
    context = {'form': form}
    return render(request, 'car_create.html', context)

def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    context = {'car': car}
    return render(request, 'car_details.html', context)

def car_edit(request, pk):
    car = Car.objects.get(pk=pk)
    form = CarModelForm(instance=car)
    if request.method == 'POST':
        form = CarModelForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('cars_app:car_details', pk=car.pk)
    context = {'form': form, 'car': car}
    return render(request, 'car_edit.html', context)

def car_delete(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('cars_app:cars_list')
    return redirect('cars_app:car_details', pk=car.pk)
