from django.contrib import admin
from django.urls import path
from core.views import home, complete_task, block_task

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", home, name="home"),

    path(
        "complete-task/<int:task_id>/",
        complete_task,
        name="complete_task"
    ),

    path(
        "block-task/<int:task_id>/",
        block_task,
        name="block_task"
    ),
]