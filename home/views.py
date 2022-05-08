from .serializers import todoserializer
from .models import todo
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from asgiref.sync import sync_to_async


# Create your views here.
@sync_to_async
@api_view(["GET", "POST", "PUT", "DELETE"])
def sendData(request):
    m = todo.objects.all().order_by("-date")
    data = todoserializer(m, many=True)
    if request.method == "GET":
        return Response(data.data)

    if request.method == 'POST':
        serializ = todoserializer(data=request.data)
        if serializ.is_valid():
            serializ.save()
            return Response(serializ.data, status=status.HTTP_201_CREATED)
        else:
            print(False)
    if request.method == "PUT":
        insta = todo.objects.get(id=request.data['id'])
        insta.title = request.data['title']
        insta.content = request.data['content']
        insta.save()
    return Response(data.data)


@api_view(["DELETE"])
def deleteTodo(request, id):
    m = todo.objects.all().order_by("-date")
    data = todoserializer(m, many=True)
    if request.method == "DELETE":
        todo.objects.filter(id=id).delete()
    return Response(data.data)
