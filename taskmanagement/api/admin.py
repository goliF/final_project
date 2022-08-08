from django.contrib import admin
from .models import Task, Status

# Register models Task & Status to see in admin
admin.site.register(Task)
admin.site.register(Status)
