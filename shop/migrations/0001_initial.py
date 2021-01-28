# Generated by Django 3.1.4 on 2020-12-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Каталог товару',
                'verbose_name_plural': 'Каталоги товарів',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_panel_name', models.CharField(default='', max_length=255, verbose_name='Назва в панеі адміністратора')),
                ('filter_name', models.CharField(blank=True, default='', max_length=255, verbose_name='Назва для фільтру')),
                ('characteristic', models.CharField(max_length=255, verbose_name='Характеристика')),
                ('value', models.CharField(max_length=255, verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'Характеристика товару',
                'verbose_name_plural': 'Характеристики товарів',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Назва товару')),
                ('slug', models.CharField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='img/products/')),
                ('description', models.TextField(blank=True, verbose_name='Опис товару')),
                ('prices', models.DecimalField(decimal_places=2, max_digits=10)),
                ('publish', models.DateField(auto_now_add=True, verbose_name='Опубліковано')),
                ('updated', models.DateField(auto_now=True, verbose_name='Оновлено')),
                ('status', models.CharField(choices=[('draft', 'В обробці'), ('published', 'Опубліковано')], default='draft', max_length=10, verbose_name='Статус')),
                ('catalog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.catalog', verbose_name='Каталог товарів')),
                ('characteristics', models.ManyToManyField(to='shop.Characteristic')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
                'ordering': ('-publish',),
            },
        ),
    ]