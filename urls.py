from django.contrib import admin
from django.urls import path, include  # ← include обов’язково

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),  # ← це підключає blog.urls
]
