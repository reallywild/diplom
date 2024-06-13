from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from .models import News, Service, Vacancy
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


def get_home(request):
    return render(request, 'home.html', context={'title': 'Главная страница'})

def get_news(request):
    news = News.objects.all().order_by('-set_time')
    return render(request, 'news/news.html', {"news": news, 'title': 'Новости'})

def services(request):
    services = Service.objects.filter()
    return render(request, 'services.html', {"services": services, 'title': 'Услуги'})

def vacancies(request):
    vacancies = Vacancy.objects.filter()
    return render(request, 'vacancies.html', {"vacancies": vacancies, 'title': 'Вакансии'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Контакты'})

class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class= RegistrationForm
    success_url = reverse_lazy('login')

# class LoginView(CreateView):
#     template_name = 'registration/login.html'
#     form_class= LoginForm
#     success_url = reverse_lazy('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            # Возвращение ошибки авторизации
            return render(request, 'registration/login.html', {'error': 'Неправильный логин или пароль'})
    else:
        return render(request, 'registration/login.html')

