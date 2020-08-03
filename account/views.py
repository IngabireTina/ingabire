from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from .models import *
from .forms import AddressForm, UserForm
from registerItem.models import *
from django.contrib.auth.models import Group


# Create your views here.
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'user'])
# @admin_only
def home(request):
    users = User.objects.all()
    item = Item.objects.all()
    stocks = Stock.objects.all()
    submitted = item.filter(status='submitted').count()
    not_work = item.filter(status='Not Work').count()
    work = item.filter(status='Work').count()

    total_users = users.count()
    total_items = item.count()
    total_device = stocks.count()

    context = {'total_users': total_users, 'total_items': total_items,
               'total_device': total_device, 'submitted': submitted, 'not_work': not_work, 'work': work}

    return render(request, 'dashboard.html', context)


# @unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='user')
            user.groups.add(group)

            messages.success(request, 'The User was successful created' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['user', 'admin'])
def userProfile(request):
    user = request.user
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration/profile.html', context)


# the login
# @unauthenticated_user
def homePage(request):
    return render(request, 'registration/home.html')


# @login_required(login_url='login')
# def logoutUser(request):
#     logout(request)
#     return redirect('login')


# display of * user
def allUser(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, 'allUsers.html', context)


# update user
def updateUser(request, pk):
    user = User.objects.get(id=pk)
    form = CreateUserForm(instance=user)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')

    context = {'form': form}
    return render(request, 'user/updateUser.html', context)


# delete user

def deleteUser(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'user': user}
    return render(request, 'user/deleteUser.html', context)


def address(request):
    form = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('address')
    addresses = Address.objects.all()

    context = {'form': form, 'addresses': addresses}
    return render(request, 'address.html', context)


# def allAddress(request):
#     addresses = Address.objects.all()
#     context = {'addresses': addresses}
#     return render(request, 'address.html', context)


def updateAddress(request, pk):
    add = Address.objects.get(id=pk)
    form = AddressForm(instance=add)
    if request.method == 'POST':
        form = AddressForm(request.method, instance=add)
        if form.is_valid():
            form.save()
            return redirect('address')

    context = {'form': form}
    return render(request, 'address/updateAddress.html', context)


def deleteAddress(request, pk):
    form = Address.objects.get(id=pk)
    if request.method == 'POST':
        form.delete()
        return redirect('address')

    context = {'form': form}
    return render(request, 'address/deleteAddress.html', context)


# the used for test
# @login_required(login_url='login')
def profile(request):
    context = {}
    return render(request, 'registration/login.html', context)


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Admin'])
def finance(request):
    return render(request, 'finance.html')
