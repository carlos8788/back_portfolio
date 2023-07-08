from rest_framework import generics
from .models import Contacto
from .serializers import ContactoSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

class ContactoPagination(PageNumberPagination):
    page_size = 5


@permission_classes([IsAuthenticatedOrReadOnly])
class ContactoListCreateView(generics.ListCreateAPIView):
    queryset = Contacto.objects.all().order_by('id')
    print(queryset)
    serializer_class = ContactoSerializer
    pagination_class = ContactoPagination

    def get_permissions(self):
        if self.request.method == 'POST':
            print(self.request)
            return [AllowAny()]
        print("Request method is not POST")
        return super().get_permissions()
    
    @action(detail=True, methods=['post'])
    def custom_action(self, request, pk=None):
        # Lógica de tu acción personalizada
        return Response({'message': 'Custom action executed'})

