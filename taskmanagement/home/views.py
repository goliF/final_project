from django.shortcuts import render
from django.views import View
from django.conf import settings


# A simple view for home with main.html ui page.
class HomeView(View):
    def get(self, request):
        return render(request, 'home/main.html')

