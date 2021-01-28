from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField(
        label='Введіть email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Введіть пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email').strip()
        password = self.cleaned_data.get('password').strip()

        if email and password:
            qs = User.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('Такого користувача не існує в системі!')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Пароль не вірний!')

            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError('Даний користувач не активний у системі!')

        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
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
    phone_number = forms.CharField(
        label="Номер телефону",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True,
    )
    email = forms.EmailField(
        label='Email-адреса',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password = forms.CharField(
        label='Введіть пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    password2 = forms.CharField(
        label='Введіть пароль ще раз',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'phone_number', 'email',)

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Паролі не співпадають!')

        return data['password2']


class CustomChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Введіть старий пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    new_password1 = forms.CharField(
        label='Введіть новий пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )
    new_password2 = forms.CharField(
        label='Введіть новий пароль ще раз',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=True,
    )

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2',)