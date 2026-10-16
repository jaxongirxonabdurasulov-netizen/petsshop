from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Product, ANIMAL_CHOICES
from .forms import AppointmentForm


def product_list(request):
    animal = request.GET.get('animal')
    products = Product.objects.all()
    if animal:
        products = products.filter(animal=animal)
    return render(request, 'shop/product_list.html', {
        'products': products,
        'animals': ANIMAL_CHOICES,
        'selected': animal,
    })

def appointment(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shop:product_list')
    return render(request, 'shop/appointment.html', {'form': form})