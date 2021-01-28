from django.db import models
from django.conf import settings

from shop.models import Product

# Create your models here.

class Order(models.Model):

    ORDER_STATUS = (
        ('Прийнятий', 'Прийнятий'),
        ('Виконаний', 'Виконаний'),
        ('В обробці', 'В обробці'),
        ('Скасований', 'Скасований'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='', blank=True)
    f_name = models.CharField(max_length=50, null=True, verbose_name="Ім'я")
    l_name = models.CharField(max_length=50, null=True, verbose_name='Прізвище')
    email = models.EmailField(null=True, verbose_name='Email-адреса')
    city = models.CharField(max_length=50, verbose_name='Місто', null=True)
    address = models.CharField(max_length=100, verbose_name='Адреса', null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено', null=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено', null=True)
    paid = models.BooleanField(default=False, verbose_name='Оплачено', null=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='Прийнятий', verbose_name='Статус')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Списки замовлень'

    def __str__(self):
        return f'Замовлення №{self.id}'
        return self.get_status_display()

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кількість')

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
