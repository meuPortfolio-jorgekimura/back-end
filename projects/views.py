from rest_framework import generics
from .models import Project, Link
from .serializers import ProjectSerializer


class ProjectView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(links=self.request.data['links'])
