from django.urls import path
from .appviews.auth_views import SignupView, UserDetailsView
from .appviews.task_views import TodoCreateView, TodoListView, TodoUpdateView, TodoDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Authentication Endpoints
    path('signup/', SignupView.as_view(), name='signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailsView.as_view(), name='user_details'),
    # Task CRUD Endpoints 
    path('todos/', TodoListView.as_view(), name='todo_list'),  # GET all tasks
    path('todos/create/', TodoCreateView.as_view(), name='todo_create'),  # POST create new task
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),  # PATCH update task status
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),  # DELETE delete task
]
