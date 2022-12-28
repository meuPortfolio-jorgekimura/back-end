from django.urls import path
from . import views
from techs import views as tech_view

urlpatterns = [
    path("projects/", views.ProjectView.as_view()),
    path("techs/", tech_view.TechView.as_view()),
]
