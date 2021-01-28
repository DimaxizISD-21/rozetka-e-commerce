from django.db import models

# Create your models here.

class Catalog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва")
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        verbose_name = 'Каталог товару'
        verbose_name_plural = 'Каталоги товарів'

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    admin_panel_name = models.CharField(max_length=255, verbose_name='Назва в панеі адміністратора', default='')
    filter_name = models.CharField(max_length=255, verbose_name='Назва для фільтру', default='', blank=True)
    characteristic = models.CharField(max_length=255, verbose_name='Назва')
    value = models.CharField(max_length=255, verbose_name='Значення')

    class Meta:
        verbose_name='Характеристика товару'
        verbose_name_plural = 'Характеристики товарів'

    def __str__(self):
        return self.admin_panel_name


class Product(models.Model):
    CHOICE_STATUS = (
        ('draft', 'В обробці'),
        ('published', 'Опубліковано')
    )

    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='Каталог товарів')
    product_name = models.CharField(max_length=100, verbose_name="Назва товару")
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to='img/products/', blank=True)
    description = models.TextField(verbose_name='Опис товару', blank=True)
    characteristics = models.ManyToManyField(Characteristic, verbose_name='Характеристики')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    publish = models.DateField(editable=True, auto_now_add=True, verbose_name='Опубліковано')
    updated = models.DateField(editable=True, auto_now=True, verbose_name='Оновлено')
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default='draft', verbose_name='Статус')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('-publish',)

    def __str__(self):
        return self.product_name

