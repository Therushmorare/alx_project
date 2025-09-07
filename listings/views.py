from django.http import JsonResponse

def api_overview(request):
    return JsonResponse({
        "message": "Welcome to the Listings API 🚀",
        "endpoints": {
            "listings/": "List all properties",
            "swagger/": "API documentation"
        }
    })

