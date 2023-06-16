from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def my_view(request: HttpRequest) -> HttpResponse:
    # Acceder a los datos de la solicitud
    query_params = request.GET
    form_data = request.POST
    method = request.method
    path = request.path
    headers = request.headers
    user = request.user

    # Realizar acciones basadas en los datos de la solicitud

    # Devolver una respuesta HTTP
    return HttpResponse("Hello, World!")

# Create your views here.
