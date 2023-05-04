from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('landing_page.urls'), name='home'),
    path('clientes/', include('clientes.urls'), name='clientes'),
    path('admin/', admin.site.urls),
]
