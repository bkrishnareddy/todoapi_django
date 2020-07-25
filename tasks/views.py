from django.shortcuts import render
from django.http import JsonResponse
from tasks.models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TaskSerializer


# Create your views here.
@api_view(['GET'])
def taskOverview(request):
    api_urls = {
        "List": "/task-list/",
        "Detail View": "/task-detail/<str:PK>",
        "Create": "/task-create/",
        "Update": "/task-update/<str:PK>",
        "Delete": "/task-delete/<str:PK>"
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    all_tasks = Task.objects.all()
    serializer = TaskSerializer(all_tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item Delted")
