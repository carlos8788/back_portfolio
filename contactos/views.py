from rest_framework import generics
from .models import Contacto
from .serializers import ContactoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


class ContactoPagination(PageNumberPagination):
    page_size = 5


@permission_classes([IsAuthenticatedOrReadOnly])
class ContactoListCreateView(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class = ContactoSerializer
    pagination_class = ContactoPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [AllowAny()]
        return super().get_permissions()


