from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User


def register(request):
    data = request.POST
    username = data.get("username", "").strip()
    password = data.get("password", "").strip()
    password_confirm = data.get("confirm_password", "").strip()
    if not username or not password or not password_confirm:
        return JsonResponse({
            "result": "Username or password cannot be empty, please try again."
        })
    if password != password_confirm:
        return JsonResponse({
            "result": "Password does not match, please try again."
        })
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "result": "Username already exists, please try again."
        })
    user = User.objects.create_user(username=username, password=password)
    user.set_password(password)
    user.save()
    login(request, user)
    return JsonResponse({
        "result": "success"
    })