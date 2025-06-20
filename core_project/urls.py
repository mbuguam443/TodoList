from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import include

def create_super(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('create-superuser/', create_super),  # 👈 TEMPORARY route
]
