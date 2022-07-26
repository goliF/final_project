from django.urls import include, path, reverse_lazy

from task import views

app_name = 'tasks'


# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined
# url patterns for task list, create, update & delete tasks in separate API endpoints.
# Each endpoint has its own ui page with bootstrap and html, CSS.
urlpatterns = [
    path('', views.TaskListView.as_view(), name='all'),
    path('create',
         views.TaskCreateView.as_view(success_url=reverse_lazy('tasks:all')), name='task_create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/update',
         views.TaskUpdateView.as_view(success_url=reverse_lazy('tasks:all')), name='task_update'),
    path('<int:pk>/delete',
         views.TaskDeleteView.as_view(success_url=reverse_lazy('tasks:all')), name='task_delete'),
    path('<int:pk>/status',
         views.StatusCreateView.as_view(), name='status_updated'),
]

