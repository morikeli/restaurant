from .forms import AddNewFoodForm, AddNewTableForm, PlaceFoodOrderForm
from .models import Food, Tables, FoodOrders, BookTable
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def available_foods_view(request):
    form = AddNewFoodForm()

    if request.method == 'POST':
        form = AddNewFoodForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'Food record created and saved successfully!')
            return redirect('')


    context = {'AddNewFoodForm': form}
    return render(request, 'users/', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def restaurant_tables_view(request):
    form = AddNewTableForm()

    if request.method == 'POST':
        form = AddNewTableForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Table record created and saved successfully!')
            return redirect('')

    context = {}
    return render(request, 'users/', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def food_orders_view(request, food_order):
    order = FoodOrders.objects.get(id=food_order)
    form = PlaceFoodOrderForm()

    if request.method == 'POST':
        form = PlaceFoodOrderForm(request.POST)

        if form.is_valid():
            new_order_record = form.save(commit=False)
            new_order_record.customer = request.user
            new_order_record.food = order
            new_order_record.save()

            messages.success(request, 'Food order submitted successfully!')
            return redirect('')

    context = {}
    return render(request, 'users/', context)