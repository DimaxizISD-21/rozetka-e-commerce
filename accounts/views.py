from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, View
from accounts.forms import UserLoginForm, UserRegistrationForm, CustomChangePasswordForm
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.urls import reverse_lazy
from orders.models import Order
from django.contrib.auth.views import PasswordChangeView

# Create your views here.

User = get_user_model()

class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['orders_list'] = Order.objects.filter(user=self.request.user)
        return context


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        email = data.get('email')
        password = data.get('password')
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)
        return redirect('accounts:profile')


class LogoutView(View):

    def get(self, *args):
        logout(self.request)
        return redirect('accounts:login')


class RegistrationView(FormView):
    template_name = 'accounts/registration.html'
    form_class = UserRegistrationForm

    def form_valid(self, form):
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(self.request, 'accounts/registration_done.html', {'form': form})


class CustomChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    form_class = CustomChangePasswordForm
    success_url = reverse_lazy('accounts:profile')
