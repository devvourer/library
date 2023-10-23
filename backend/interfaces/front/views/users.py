from django.views.generic import TemplateView
from django.shortcuts import redirect, reverse, render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


from interfaces.front.forms.users import LoginForm, RegisterForm, VerifyEmailForm


class Login(TemplateView):
    template_name = 'users/login.html'

    def get_context(self, **kwargs):
        return {
            'form': LoginForm(),
        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('website:main'))
        return render(request, self.template_name, self.get_context())

    def post(self, request: HttpResponse) -> HttpResponse:
        form = LoginForm(request.POST)
        if not form.is_valid():
            raise ...

        email = form.data['email']
        password = form.data['password']
        authenticated_user = authenticate(request=request, email=email, password=password)

        if not authenticated_user:
            messages.error(request, 'Invalid email or password')
            return redirect('user:login')

        login(request, authenticated_user)
        return redirect(reverse('website:main'))


class Register(TemplateView):
    template_name = 'users/registration.html'

    def get_context(self, form=None, **kwargs):
        return {
            'form': form or RegisterForm(),
        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('website:main'))
        return render(request, self.template_name, self.get_context())

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, self.get_context(form=form))

        form.save()
        return redirect(reverse('user:login'))


class VerifyEmail(TemplateView):
    template_name = 'users/verify_email.html'





