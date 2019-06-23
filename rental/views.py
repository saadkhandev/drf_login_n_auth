from rest_framework import viewsets, permissions
from rental.models import Friend, Belonging, Borrowed
from rental.serializers import FriendSerializer, BelongingSerializer, BorrowedSerializer
from .permissions import IsOwner


class FriendViewSet(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    permission_classes = [IsOwner]


class BelongingViewSet(viewsets.ModelViewSet):
    queryset = Belonging.objects.all()
    serializer_class = BelongingSerializer


class BorrowedViewSet(viewsets.ModelViewSet):
    queryset = Borrowed.objects.all()
    serializer_class = BorrowedSerializer


class MyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.DjangoModelPermissions]