from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


# def login_view(request):
#     context = {}
#     user = request.user
#     if user.is_authenticated:
#         return redirect('home')
#     if request.POST:
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             # login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             email = request.POST['Email']
#             password = request.POST['Password']
#             user = authenticate(request, email=email, password=password)
#             if user:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = AuthenticationForm()
#     context['login_form'] = form
#     return render(request, 'login.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    else:
        return render(request, 'login.html')


# from django.shortcuts import render
#
# # Create your views here.
# from django.urls import reverse_lazy
# from django.views.generic.edit import CreateView
# from .forms import CustomUserCreationForm
#
#
# class TeamSignUp(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('home')
#     template_name = 'register.html'

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from authentication.forms import RegistrationForm
#
#
# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=email, password=raw_password)
#             login(request, account)
#             return redirect('home')
#         else:
#             context['registration_form'] = form
#     else:  # GET request
#         form = RegistrationForm()
#         context['registration_form'] = form
#     return render(request, 'register.html', context)
#
#
#
#



# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from authentication.forms import RegistrationForm
#
#
# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             email = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             account = authenticate(email=email, password=raw_password)
#             login(request, account)
#             return redirect('home')
#         else:
#             context['registration_form'] = form
#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form
#     return render(request, 'register.html', context)
#
#
# def logout_view(request):
#     logout(request)
#     return redirect('home')



