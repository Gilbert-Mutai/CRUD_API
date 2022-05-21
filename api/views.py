from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


# @api_view(['GET'])
# def apiOverview(request):
#     tasks = [
#             {
#                 "id": 1,
#                 "title": "",
#                 "code": "foo = \"bar\"\n",
#                 "linenos": False,
#                 "language": "python",
#                 "style": "friendly"
#             },
#             {
#                 "id": 2,
#                 "title": "",
#                 "code": "print(\"hello, world\")\n",
#                 "linenos": False,
#                 "language": "python",
#                 "style": "friendly"
#             }
#             ]
#     return Response(tasks)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data= request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk) 
    task.delete()

    return Response("Item deleted successfully")

