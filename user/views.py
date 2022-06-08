from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from rest_framework.response import Response


# Create your views here.
class LoginAPIView(generics.GenericAPIView):
    """Login View"""
    serializer_class = LoginSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)

        return Response(serializers.data, status=status.HTTP_200_OK)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    permission_classes =[IsAuthenticated]