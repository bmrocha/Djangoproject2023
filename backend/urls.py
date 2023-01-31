from django.contrib import admin
# incluido include e path informamos modulo.
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
]
