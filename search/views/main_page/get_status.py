from django.http import JsonResponse


def get_status(request):
    user = request.user
    if user.is_authenticated:
        return JsonResponse({
            "result": "logged_in",
            "username": user.username
        })
    return JsonResponse({
        "result": "logged_out",
    })
