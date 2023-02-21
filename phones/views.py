from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    template = 'catalog.html'
    request_get = request.GET.get('sort')

    if request_get == 'name':
        phones = phones.order_by('name')
    if request_get == 'min_price':
        phones = phones.order_by('price')
    if request_get == 'max_price':
        phones = phones.order_by('-price')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)
