from .forms import AddNewFoodForm, AddNewTableForm, PlaceFoodOrderForm, TableBookingForm
from .models import Food, Tables, FoodOrders, BookTable
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib import messages


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def add_new_food_view(request):
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
def edit_available_foods_view(request, id):
    food_obj = Food.objects.get(id=id)
    form = AddNewFoodForm(instance=food_obj)

    if request.method == 'POST':
        form = AddNewFoodForm(request.POST, request.FILES, instance=food_obj)

        if form.is_valid():
            form.save()
            messages.info(request, 'You have updated details for this food')
            return redirect('update_food_details', id)


    context = {'EditForm': form}
    return render(request, 'users/', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def edit_tables_info_view(request, id):
    table_obj = Tables.objects.get(id=id)
    form = AddNewTableForm(instance=table_obj)

    if request.method == 'POST':
        form = AddNewTableForm(request.POST, request.FILES, instance=table_obj)

        if form.is_valid():
            form.save()
            messages.warning(request, 'You have updated details for this table')
            return redirect('update_table_info', id)


    context = {'EditForm': form}
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

    context = {'form': form}
    return render(request, 'users/', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_staff is True and user.is_superuser is False)
def table_booking_view(request, table):
    table_obj = Tables.objects.get(id=table)
    form = TableBookingForm()

    if request.method == 'POST':
        form = TableBookingForm(request.POST)

        if form.is_valid():
            new_booking = form.save(commit=False)
            new_booking.customer = request.user
            new_booking.table_no = table_obj
            new_booking.save()

            messages.success(request, 'Table booked successfully!')
            return redirect('')

    context = {'form': form}
    return render(request, 'users/', context)