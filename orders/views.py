from django.shortcuts import render, redirect
from cart.cart import Cart
from orders.forms import CreateOrderForm
from orders.models import OrderItem, Order

# Create your views here.

def order_create_view(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            cart.clear()
            return redirect('accounts:profile')

    else:
        if request.user.is_authenticated == True:
            form = CreateOrderForm(initial = {
                'f_name': request.user.f_name,
                'l_name': request.user.l_name,
                'email': request.user.email,
            })
        else:
            form = CreateOrderForm()

    return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})
