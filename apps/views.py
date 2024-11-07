from logging import root

from django.shortcuts import render, redirect
from django.utils.text import slugify

import root
from apps.forms import ChoiceForm
from apps.models import Category, Shoes, Buy


def home(request):
    ctg = Category.objects.all()
    shoes = Shoes.objects.all()
    ctx = {
        'ctg': ctg,
        'shoes': shoes
    }
    return render(request, 'apps/index.html', ctx)


def contact(request):
    ctx = {}
    return render(request, 'apps/contact.html', ctx)


def products(request, slug=None):
    ctg = Category.objects.all()
    category = Category.objects.get(slug=slug)
    shoes = Shoes.objects.all().filter(type_id=category.id)
    ctx = {
        'ctg': ctg,
        'category': category,
        'shoes': shoes
    }
    return render(request, 'apps/products.html', ctx)


def register(request):
    ctx = {}
    return render(request, 'apps/register.html', ctx)


def single(request, pk=None):
    ctg = Category.objects.all()
    product_pk = Shoes.objects.get(pk=pk)
    form = ChoiceForm
    if request.POST:
        forms = ChoiceForm(request.POST or None, request.FILES or None)
        if forms.is_valid():
            root = forms.save()
            root = Buy.objects.get(pk=root.id)
            root.product = product_pk
            root.save()
            return redirect('home')
        else:
            print(forms.errors)

    ctx = {
        'ctg': ctg,
        'product_pk': product_pk,
        'form': form

    }
    return render(request, 'apps/single.html', ctx)
