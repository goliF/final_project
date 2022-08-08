from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from rest_framework import status

from .models import Task, Status
from .serializers import TaskSerializer, StatusSerializer
from .permissions import IsOwner


# Task list & create view
class ListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

# Task detail,update,delete view
class DetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskSerializer

    # Task detail
    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task_serializer = TaskSerializer(task)
        return Response(task_serializer.data)

    # Update task
    def put(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete task
    def delete(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Status view
class StatusDetail(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = StatusSerializer

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        if request.user == task.owner:
            status_list = Status.objects.filter(task=task)
            status_serializer = StatusSerializer(status_list, many=True)
            return Response(status_serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request, pk):
        t = get_object_or_404(Task, id=pk)
        s = request.POST.get('status')
        status = Status(status=s, task=t, owner=request.user)
        status.save()
        return redirect(reverse('api:status', args=[t.id]))
