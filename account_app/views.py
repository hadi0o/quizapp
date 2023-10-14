from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import View
from .forms import LoginForm, RegisterForm
from .models import Profile
from django.contrib import messages


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('quiz:quiz_page')
        else:
            form = LoginForm()
            return render(request, 'account_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['fullname'], password=cd['password'])

            if user is not None:
                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return redirect('quiz:quiz_page')
            else:
                form.add_error('fullname', 'Invalid User Data')

        return render(request, 'account_app/login.html', {'form': form})


class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('quiz:quiz_page')
        else:
            form = RegisterForm()
            return render(request, 'account_app/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            if cd['password'] != cd['conf_pass']:
                form.add_error('password', 'Passwords are not the same !!')
            else:
                fullname = f"{cd['first_name']} {cd['last_name']}"

                user = User.objects.create_user(
                    username=fullname,
                    first_name=cd['first_name'],
                    last_name=cd['last_name'],
                    email=cd['email'],
                    password=cd['password'],)

                login(request, user, backend="django.contrib.auth.backends.ModelBackend")
                return redirect('quiz:quiz_page')
        else:
            form.add_error('password', 'Invalid Data')

        return render(request, 'account_app/register.html', {'form': form})


def profile_view(request):
    if request.method == 'POST':
        namea = request.POST.get('name')
        tela = request.POST.get('tel')
        sexa = request.POST.get('sex')
        agea = request.POST.get('age')
        field = request.POST.get('field')
        citya = request.POST.get('city')
        sleep = request.POST.get('sleep')

        try:
            profile = Profile(name=namea, tel=tela, sex=sexa,
                              age=agea, field_of_study=field,
                              city=citya, sleep_time=sleep)
            profile.save()

            success = True
            message = "ثبت اطلاعات با موفقیت انجام شد"

        except Exception as e:
            message = str(e)

        response_data = {
            "success": success,
            "message": message
        }
        return JsonResponse(response_data)
    else:
        return render(request, 'account_app/profile.html')
