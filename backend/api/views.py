from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    return JsonResponse({
        "msg": "dDjango API response"
    })


def api_query(request, *args, **kwargs):
    return JsonResponse({
        "msg": "dDjango query"
    })
