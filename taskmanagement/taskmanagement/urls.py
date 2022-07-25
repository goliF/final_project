from django.contrib import admin
from django.urls import path, include

# Here home, default login, task url patterns has been defined.
urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('tasks/', include('task.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]
