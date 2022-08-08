from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Task, Status
from .serializers import TaskSerializer, StatusSerializer


# Task list view
class TaskListView(APIView):
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/list.html'

    def get(self, request):
        # search query handling
        strval = request.GET.get("search", False)
        if strval:
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval)
            query.add(Q(description__icontains=strval), Q.OR)
            tasks = (Task.objects.filter(query)).select_related().order_by('-updated_at')[:10]
        else:
            tasks = Task.objects.all().order_by('-updated_at')[:10]
        for obj in tasks:
            obj.natural_updated = naturaltime(obj.updated_at)
        ctx = {'task_list': tasks, 'search': strval}
        return Response(ctx)


# Task detail view
class TaskDetailView(APIView):
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    serializer_class = TaskSerializer
    template_name = "task/detail.html"

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        status_list = Status.objects.filter(task=task).order_by('-updated_at')
        status_serializer = StatusSerializer()
        ctx = {'task': task, 'status_list': status_list, 'status_serializer': status_serializer,
               "choices": Status.status_list}
        return Response(ctx)


# Create task view
class TaskCreateView(LoginRequiredMixin, APIView):
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks:all')

    def get(self, request, pk=None):
        serializer = TaskSerializer()
        ctx = {'serializer': serializer}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return redirect(self.success_url)
        ctx = {'serializer': serializer}
        return render(request, self.template_name, ctx)


# Update task view
class TaskUpdateView(LoginRequiredMixin, APIView):
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks:all')

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=self.request.user)
        serializer = TaskSerializer(instance=task)
        ctx = {'serializer': serializer}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        task = get_object_or_404(Task, id=pk, owner=self.request.user)
        serializer = TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return redirect(self.success_url)
        ctx = {'serializer': serializer}
        return render(request, self.template_name, ctx)


# Delete task view
class TaskDeleteView(LoginRequiredMixin, APIView):
    queryset = Task.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'task/task_delete.html'
    success_url = reverse_lazy('tasks:all')

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=self.request.user)
        ctx = {'task': task}
        return render(request, self.template_name, ctx)

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk, owner=self.request.user)
        task.delete()
        return redirect(self.success_url)


# Status view
class StatusCreateView(LoginRequiredMixin, APIView):
    queryset = Status.objects.all()

    def get(self, request, pk):
        return redirect(reverse('tasks:task_detail', args=[pk]))

    def post(self, request, pk):
        t = get_object_or_404(Task, id=pk)
        s = request.POST.get('status')
        status = Status(status=s, task=t, owner=request.user)
        status.save()
        return redirect(reverse('tasks:task_detail', args=[t.id]))
