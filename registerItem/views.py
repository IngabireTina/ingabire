from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm
from .forms import StockForm
from .models import Stock
from account.models import User


# Create your views here.
def recordItem(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    items = Item.objects.all()

    context = {'form': form, 'items': items}
    return render(request, 'registerItem.html', context)


def allItem(request):
    item = Item.objects.all()
    context = {'item': item}
    return render(request, 'dashboard.html', context)


def updateItem(request, pk):
    item = Item.objects.get(id=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'updateItem.html', context)


def deleteItem(request, pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')

    context = {'item': item}
    return render(request, 'deleteItem.html', context)


# the stock record
def recordStock(request):
    form = StockForm()
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'stock/recordStock.html', context)


def allStock(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/allStock.html', context)


def updateStock(request, pk):
    stock = Stock.objects.get(id=pk)
    form = StockForm(instance=stock)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('allstock')

    context = {'form': form}
    return render(request, 'stock/updateStock.html', context)


def deleteStock(request, pk):
    form = Stock.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('allstock')

    context = {'form': form}
    return render(request, 'stock/deleteStock.html', context)
