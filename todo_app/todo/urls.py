

from django.urls import path
from .views import TaskList, Taskcreate, TaskUpdate, TaskDelete,TaskDetailView
from .import views
urlpatterns =[
    path('', views.Home, name='home'),
    path('login/', views.login_fun, name='login'),
    path('register/', views.register_fun, name='Register'),
    path('task-list/',TaskList.as_view(),name='task'),
    path('task-create/',Taskcreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
    path('task-detail/<int:pk>/',TaskDetailView.as_view(),name='task-detail'),

    ]
