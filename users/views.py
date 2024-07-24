from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout

from .forms import UserRegisterForm, UserLoginForm, UserUpdateForm, UserDeleteForm
from .models import User


class UserRegisterView(views.CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login_user')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(auth_views.LoginView):
    model = User
    form_class = UserLoginForm
    template_name = 'users/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    # next_page = reverse_lazy('login_user')
    template_name = 'users/logged_out.html'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        request.session.flush()
        return response


class UserUpdateView(views.UpdateView):
    model = User
    template_name = 'users/update_profile.html'
    form_class = UserUpdateForm

    def get_success_url(self):
        return reverse_lazy('details_user', kwargs={'pk': self.object.pk})


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    model = User
    template_name = 'users/delete_profile.html'
    form_class = UserDeleteForm
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        logout(request)
        self.object.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserDeleteForm
        return context


def details_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user != request.user:
        raise PermissionDenied
    context = {
        'user': user
    }
    return render(request, 'users/details_profile.html', context)


