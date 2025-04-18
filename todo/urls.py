from django.urls import path
from .views import task_list, task_detail, SecureHelloView

urlpatterns = [
    path("tasks/", task_list, name="task_list"),
    path("tasks/<int:pk>/", task_detail, name="task_detail"),
    path('secure-hello/', SecureHelloView.as_view()),
]

