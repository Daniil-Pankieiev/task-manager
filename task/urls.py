from django.urls import path

from task.views import TaskListView, index, TaskDetailView, toggle_assign_to_task, TaskCreateView, TaskUpdateView, \
    TaskDeleteView, WorkerListView, WorkerDetailView, WorkerDeleteView, WorkerUpdateView, WorkerCreateView, \
    finish_task, TaskTypeListView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView, PositionListView, \
    PositionCreateView, PositionUpdateView, PositionDeleteView

# from .views import (
#
# )



urlpatterns = [
    path("", index, name="index"),
    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list",
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign",
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="tasks-create",
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",
    ),
    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list",
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create",
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/<int:pk>/update/",
        WorkerUpdateView.as_view(),
        name="worker-update",
    ),
    path(
        "workers/<int:pk>/delete/",
        WorkerDeleteView.as_view(),
        name="worker-delete",
    ),
    path(
        "tasks/<int:pk>/finish-task/",
        finish_task,
        name="finish-task",
    ),
    path(
        "tasktypes/",
        TaskTypeListView.as_view(),
        name="tasktype-list",
    ),
    path(
        "tasktypes/create/",
        TaskTypeCreateView.as_view(),
        name="tasktype-create",
    ),
    path(
        "tasktypes/<int:pk>/update/",
        TaskTypeUpdateView.as_view(),
        name="tasktype-update",
    ),
    path(
        "tasktypes/<int:pk>/delete/",
        TaskTypeDeleteView.as_view(),
        name="tasktype-delete",
    ),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list",
    ),
    path(
        "position/create/",
        PositionCreateView.as_view(),
        name="position-create",
    ),
    path(
        "position/<int:pk>/update/",
        PositionUpdateView.as_view(),
        name="position-update",
    ),
    path(
        "position/<int:pk>/delete/",
        PositionDeleteView.as_view(),
        name="position-delete",
    ),
]

app_name = "task"
