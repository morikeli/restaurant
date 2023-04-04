from django.urls import path
from . import views

urlpatterns = [
    path('<str:id>/update-table-description/', views.edit_available_foods_view, name='update_food_details'),
    path('<str:id>/update-table-info/', views.edit_tables_info_view, name='update_table_info'),
    path('add-food-record/', views.add_new_food_view, name='foods'),
    path('add-table-record/', views.restaurant_tables_view, name='tables'),
    path('place-food-order/', views.food_orders_view, name='place_order'),
    path('<str:table>/book-table/', views.table_booking_view, name='book_table'),

]