from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import NotFound
from tasks.models import Task
from .serializers import TaskSerializer
from core.functions import api_response_data

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def task_list_create(request):
    user = request.user
    if request.method == 'GET':
        status = request.query_params.get('status')
        priority = request.query_params.get('priority')
        q = request.query_params.get('q')
        
        tasks = Task.objects.filter(user=user)
        
        if status:
            tasks = tasks.filter(status=status)
        if priority:
            tasks = tasks.filter(priority=priority)
        if q:
            tasks = tasks.filter(title__icontains=q)
            
        serializer = TaskSerializer(tasks, many=True)
        return api_response_data(
            status_code=6000,
            message="Tasks retrieved successfully",
            data=serializer.data
        )
    
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return api_response_data(
                status_code=6000,
                message="Task created successfully",
                data=serializer.data
            )
        return api_response_data(
            status_code=6001,
            message="Failed to create task",
            data=serializer.errors
        )

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def task_detail(request, task_id):
    user = request.user
    try:
        task = Task.objects.get(id=task_id, user=user)
    except Task.DoesNotExist:
        return api_response_data(
            status_code=6001,
            message="Task not found",
            data={}
        )

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return api_response_data(
            status_code=6000,
            message="Task retrieved successfully",
            data=serializer.data
        )

    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return api_response_data(
                status_code=6000,
                message="Task updated successfully",
                data=serializer.data
            )
        return api_response_data(
            status_code=6001,
            message="Failed to update task",
            data=serializer.errors
        )

    elif request.method == 'DELETE':
        task.delete()
        return api_response_data(
            status_code=6000,
            message="Task deleted successfully",
            data={}
        )
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_count(request):
    user = request.user
    total_tasks = Task.objects.filter(user=user).count()
    completed_tasks = Task.objects.filter(user=user, status='completed').count()
    pending_tasks = Task.objects.filter(user=user, status='pending').count()
    in_progress_tasks = Task.objects.filter(user=user, status='in_progress').count()
    return api_response_data(
        status_code=6000,
        message="Dashboard count retrieved successfully",
        data={
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "in_progress_tasks": in_progress_tasks,
        }
    )