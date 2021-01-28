from django.urls import path
from shop.views import (
    HomeView,
    NotebookPcView,
    PobutovaTechnikaView,
    TovariDlyaDomuView,
    SportZahoplennyaView,
    SmartphoneElektronicaView,
    ProductDetailView,
    SearchView
)

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('noutbuki-ta-kompyuteri/', NotebookPcView.as_view(), name='noutbuki-ta-kompyuteri'),
    path('pobutova-tehnika/', PobutovaTechnikaView.as_view(), name='pobutova-tehnika'),
    path('tovari-dlya-domu/', TovariDlyaDomuView.as_view(), name='tovari-dlya-domu'),
    path('sport-i-zahoplennya/', SportZahoplennyaView.as_view(), name='sport-i-zahoplennya'),
    path('smartfoni-tv-i-elektornika/', SmartphoneElektronicaView.as_view(), name='smartfoni-tv-i-elektornika'),
    path('product_detail/<slug:catalog_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('search/', SearchView.as_view(), name='search'),
]
