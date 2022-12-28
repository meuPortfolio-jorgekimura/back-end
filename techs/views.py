from rest_framework import generics
from .models import Tech
from .serializers import TechSerializer


class TechView(generics.ListCreateAPIView):
    queryset = Tech.objects.all()
    serializer_class = TechSerializer
