from django.urls import path
from todoapp import views

urlpatterns = [
    path("",views.home,name="home"),
    path("edit-task/<int:task_id>/",views.editTask,name="edit_task"),
    path("about-us/", views.about,name="about"),
    path("contact-us/",views.contact,name="contact"),
    path("delete-task/<int:task_id>/",views.deleteTask,name="delete_task")
]
