from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Todo
from ..serializers import TodoSerializer

class TodoCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can create tasks

    def post(self, request):
        title = request.data.get("title")
        
        if not title:
            return Response({"error": "Title is required"}, status=status.HTTP_400_BAD_REQUEST)

        todo = Todo.objects.create(user=request.user, title=title)
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)

class TodoListView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can view their tasks

    def get(self, request):
        todos = Todo.objects.filter(user=request.user)  # Get todos for the logged-in user
        return Response(TodoSerializer(todos, many=True).data, status=status.HTTP_200_OK)

class TodoUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can update their tasks

    def patch(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk, user=request.user)  # Find the task by ID and user
        except Todo.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        # Update the task status or other fields
        completed = request.data.get("completed", None)
        if completed is not None:
            todo.completed = completed
        todo.save()

        return Response(TodoSerializer(todo).data, status=status.HTTP_200_OK)

class TodoDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete their tasks

    def delete(self, request, pk):
        try:
            todo = Todo.objects.get(id=pk, user=request.user)  # Find the task by ID and user
        except Todo.DoesNotExist:
            return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

        todo.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
