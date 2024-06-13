from django.urls import path
from django.contrib.auth import views as dj_view
from .views import RegistrationView, login_view, get_news, get_home, services, vacancies, contact


urlpatterns = [
    path("register/", RegistrationView.as_view(), name='registration'),
    path("login/", login_view, name='login'),
    path("logout/", dj_view.LogoutView.as_view(), name='logout'),
    path("news/", get_news, name='news'),
    path("", get_home, name='home'),
    path("services/", services, name='services'),
    path("vacanies/", vacancies, name='vacancies'),
    path("contact/", contact, name='contact'),
]