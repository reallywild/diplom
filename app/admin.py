from django.contrib import admin
from .models import User, News, Service, Vacancy

# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Service)
admin.site.register(Vacancy)