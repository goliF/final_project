from django.urls import path

from api import views

app_name = 'api'


# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
# url patterns for task list, create, update & delete tasks in separate API endpoints.
# Each endpoint has its own ui page with bootstrap and html, CSS.
urlpatterns = [
    path('tasks/', views.ListView.as_view(), name='list'),
    path('tasks/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('tasks/<int:pk>/status',
         views.StatusDetail.as_view(), name='status'),
]
