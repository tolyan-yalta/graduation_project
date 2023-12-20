from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy

from users_app.forms import LoginUserForm, RegisterUserForm


class LoginUser(LoginView):
    # form_class = AuthenticationForm   
    form_class = LoginUserForm
    template_name = 'users_app/login.html'
    extra_context = {'title': "Авторизация"}

    # def get_success_url(self):
    #     # return reverse_lazy('home')
    #     return reverse_lazy('catalog')
    

# def login_user(request):
#     # return HttpResponse("login")
#     # form = LoginUserForm()
#     # return render(request, 'users_app/login.html', {'form': form})
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], 
#                                 password=cd['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 # return HttpResponseRedirect(reverse('home'))
#                 return HttpResponseRedirect(reverse('about'))
#                 # return HttpResponseRedirect(reverse('catalog:catalog'))          
    # else:
    #     form = LoginUserForm()
    # return render(request, 'users_app/login.html', {'form': form})


def logout_user(request):
    logout(request)
    # return HttpResponseRedirect(reverse('users:login'))
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users_app/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users_app/register.html', {'form': form})
