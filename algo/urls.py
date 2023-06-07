from django.urls import path

from . import views

app_name = "algo"
urlpatterns = [
    # ex: /algo/
    path("", views.index, name="index"),
    # ex: /algo/task/
    path("task/", views.task, name="task"),
    # # ex: /algo/task_result/5/
    # path("task_result/<int:pk>/", views.TaskResultView.as_view(), name="task_result"),
    # # ex: /algo/history/
    # path("history/", views.history, name="history"),
]
