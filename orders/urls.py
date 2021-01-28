from django.urls import path
from orders.views import order_create_view

app_name = 'orders'

urlpatterns = [
    path('create-order/', order_create_view, name='create-order'),
]