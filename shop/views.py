from shop.models import Product, Characteristic
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Q
from cart.forms import CartAddProductForm

# Create your views here.

class HomeView(ListView, FormView):

    template_name = 'shop/home.html'
    context_object_name = 'product_list'
    paginate_by = 8
    form_class = CartAddProductForm

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context

class CharactericsticsView():

    ##### NotebookPcView filter #####

    def get_manufacturer(self):
        return Characteristic.objects.filter(filter_name='get_manufacturer_pcnout')

    def get_cpu(self):
        return Characteristic.objects.filter(filter_name='get_cpu_pcnout')

    def get_gpu(self):
        return Characteristic.objects.filter(filter_name='get_gpu_pcnout')

    def get_ram(self):
        return Characteristic.objects.filter(filter_name='get_ram_pcnout')

    def get_hdd(self):
        return Characteristic.objects.filter(filter_name='get_hdd_pcnout')

    def get_weight(self):
        return Characteristic.objects.filter(filter_name='get_weight_pcnout')

    def get_sizes(self):
        return Characteristic.objects.filter(filter_name='sizes')

    def get_powersupply(self):
        return Characteristic.objects.filter(filter_name='get_powersupply_pcnout')


    ##### PobutovaTechnikaView filter #####

    def get_pob_manufacturer(self):
        return Characteristic.objects.filter(filter_name='get_pob_manufacturer')


    ##### TovariDlyaDomuView filter #####

    def get_tov_manufacturer(self):
        return Characteristic.objects.filter(filter_name='get_tov_manufacturer')


    ##### SportZahoplennyaView filter #####

    def get_sport_manufacturer(self):
        return Characteristic.objects.filter(filter_name='get_sport_manufacturer')


    ##### SmartphoneElektronicaView filter #####

    def get_smartelectron_manufacturer(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_manufacturer')

    def get_smartelectron_cpu(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_cpu')

    def get_smartelectron_weight(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_weight')

    def get_smartelectron_screen_size(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_screen_size')

    def get_smartelectron_matrix_type(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_matrix_type')

    def get_smartelectron_harddrive(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_harddrive')

    def get_smartelectron_ram_size(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_ram_size')

    def get_smartelectron_os(self):
        return Characteristic.objects.filter(filter_name='get_smartelectron_os')



class NotebookPcView(CharactericsticsView, ListView, FormView):

    template_name = 'shop/noutbuki-ta-kompyuteri.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):

        queryset = Product.objects.filter(catalog__slug='noutbuki-ta-kompyuteri')

        if self.request.GET:

            if self.request.GET.getlist('min_price'):

                min_price = self.request.GET.getlist('min_price')
                max_price = self.request.GET.getlist('max_price')

                queryset = Product.objects.filter(
                    Q(catalog__slug='noutbuki-ta-kompyuteri'),
                    Q(price__range = (min_price[0], max_price[0]))
                ).distinct()

                return queryset

            queryset = Product.objects.filter(
                Q(catalog__slug='noutbuki-ta-kompyuteri'),
                Q(characteristics__value__in = self.request.GET.getlist('manufacturer')) |
                Q(characteristics__value__in = self.request.GET.getlist('cpu')) |
                Q(characteristics__value__in = self.request.GET.getlist('gpu')) |
                Q(characteristics__value__in = self.request.GET.getlist('ram')) |
                Q(characteristics__value__in = self.request.GET.getlist('harddisk')) |
                Q(characteristics__value__in = self.request.GET.getlist('weight')) |
                Q(characteristics__value__in = self.request.GET.getlist('powersupply'))
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context


class PobutovaTechnikaView(CharactericsticsView, ListView, FormView):

    template_name = 'shop/pobutova-tehnika.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):

        queryset = Product.objects.filter(catalog__slug='pobutova-tehnika')

        if self.request.GET:

            if self.request.GET.getlist('min_price'):

                min_price = self.request.GET.getlist('min_price')
                max_price = self.request.GET.getlist('max_price')

                queryset = Product.objects.filter(
                    Q(catalog__slug='pobutova-tehnika'),
                    Q(price__range = (min_price[0], max_price[0]))
                ).distinct()

                return queryset

            queryset = Product.objects.filter(
                Q(catalog__slug='pobutova-tehnika'),
                Q(characteristics__value__in = self.request.GET.getlist('manufacturer'))
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context


class TovariDlyaDomuView(CharactericsticsView, ListView, FormView):

    template_name = 'shop/tovari-dlya-domu.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):

        queryset = Product.objects.filter(catalog__slug='tovari-dlya-domu')

        if self.request.GET:

            if self.request.GET.getlist('min_price'):

                min_price = self.request.GET.getlist('min_price')
                max_price = self.request.GET.getlist('max_price')

                queryset = Product.objects.filter(
                    Q(catalog__slug='tovari-dlya-domu'),
                    Q(price__range = (min_price[0], max_price[0]))
                ).distinct()

                return queryset

            queryset = Product.objects.filter(
                Q(catalog__slug='tovari-dlya-domu'),
                Q(characteristics__value__in = self.request.GET.getlist('manufacturer'))
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context


class SportZahoplennyaView(CharactericsticsView, ListView, FormView):

    template_name = 'shop/sport-i-zahoplennya.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):

        queryset = Product.objects.filter(catalog__slug='sport-i-zahoplennya')

        if self.request.GET:

            if self.request.GET.getlist('min_price'):
                min_price = self.request.GET.getlist('min_price')
                max_price = self.request.GET.getlist('max_price')

                queryset = Product.objects.filter(
                    Q(catalog__slug='sport-i-zahoplennya'),
                    Q(price__range=(min_price[0], max_price[0]))
                ).distinct()

                return queryset

            queryset = Product.objects.filter(
                Q(catalog__slug='sport-i-zahoplennya'),
                Q(characteristics__value__in=self.request.GET.getlist('manufacturer'))
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context


class SmartphoneElektronicaView(CharactericsticsView, ListView, FormView):

    template_name = 'shop/smartfoni-tv-i-elektornika.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):

        queryset = Product.objects.filter(catalog__slug='smartfoni-tv-i-elektornika')

        if self.request.GET:

            if self.request.GET.getlist('min_price'):

                min_price = self.request.GET.getlist('min_price')
                max_price = self.request.GET.getlist('max_price')

                queryset = Product.objects.filter(
                    Q(catalog__slug='smartfoni-tv-i-elektornika'),
                    Q(price__range = (min_price[0], max_price[0]))
                ).distinct()

                return queryset

            queryset = Product.objects.filter(
                Q(catalog__slug='smartfoni-tv-i-elektornika'),
                Q(characteristics__value__in = self.request.GET.getlist('manufacturer')) |
                Q(characteristics__value__in=self.request.GET.getlist('cpu')) |
                Q(characteristics__value__in=self.request.GET.getlist('os')) |
                Q(characteristics__value__in=self.request.GET.getlist('screen_size')) |
                Q(characteristics__value__in=self.request.GET.getlist('weight')) |
                Q(characteristics__value__in=self.request.GET.getlist('matrix_type')) |
                Q(characteristics__value__in=self.request.GET.getlist('ram_size')) |
                Q(characteristics__value__in=self.request.GET.getlist('harddrive'))
            ).distinct()

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context


# def product_detail_view(request, catalog_slug, slug):
#     product = get_object_or_404(Product, catalog__slug=catalog_slug, slug=slug)
#     context = {'product': product}
#     return render(request, 'shop/product_detail.html', context)

class ProductDetailView(DetailView, FormView):

    template_name = 'shop/product_detail.html'
    context_object_name = 'product'
    form_class = CartAddProductForm

    def get_queryset(self):
        catalog = self.kwargs.get('catalog_slug', '')
        slug = self.kwargs.get('slug', '')
        qs = Product.objects.filter(catalog__slug=catalog, slug=slug)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context



class SearchView(ListView, FormView):

    template_name = 'shop/search.html'
    context_object_name = 'product_list'
    form_class = CartAddProductForm

    def get_queryset(self):
        query = self.request.GET['query']
        qs = Product.objects.filter(product_name__icontains=query)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_form'] = self.form_class
        return context

# def search_view(request):
#     query = request.GET['query']
#     qs = Product.objects.filter(product_name__icontains=query)
#     context = {'product_list': qs}
#     return render(request, 'shop/search.html', context)
