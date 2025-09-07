from django.http import JsonResponse
from django.urls import reverse

def api_overview(request):
    """
    API Overview endpoint
    Returns a JSON response listing the available API endpoints.
    """
    endpoints = {
        "List All Properties": reverse("property-list"),  # DRF view name
        "API Documentation (Swagger)": reverse("schema-swagger-ui"),
    }

    return JsonResponse({
        "status": "success",
        "message": "Welcome to the Listings API 🚀",
        "endpoints": endpoints
    })

