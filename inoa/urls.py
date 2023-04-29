from django.contrib import admin
from landing_page.views import home
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
