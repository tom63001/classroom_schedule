from django.http import JsonResponse
from django.contrib.auth import authenticate, login


def signin(request):
    print("server: login")
    data = request.POST
    username = data.get("username", "")
    password = data.get("password", "")
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({
            "result": "Username or password is incorrect, please try again."
        })
    login(request, user)
    return JsonResponse({
        "result": "success"
    })
