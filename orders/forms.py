from django import forms
from orders.models import Order

class CreateOrderForm(forms.ModelForm):
    f_name = forms.CharField(
        label="Ім'я",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    l_name = forms.CharField(
        label='Прізвище',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    email = forms.EmailField(
        label='Email-адреса',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
    )
    city = forms.CharField(
        label='Місто',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    address = forms.CharField(
        label='Адреса',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = Order
        fields = ['f_name', 'l_name', 'email', 'city', 'address']