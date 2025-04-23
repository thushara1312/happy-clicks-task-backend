from django.urls import path
from .views import task_list_create, task_detail, dashboard_count

app_name = 'api_v1_tasks'

urlpatterns = [
    path('', task_list_create, name='task-list-create'),
    path('dashboard-count/', dashboard_count, name='dashboard_count'),
    path('<uuid:task_id>/', task_detail, name='task-detail'),
    
] 