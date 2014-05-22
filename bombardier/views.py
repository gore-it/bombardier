import datetime
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template


def news(request):
    now = datetime.datetime.now()
    t = get_template('news.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def log_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Your account is disabled")
    else:
        return HttpResponse("Invalid login")


def logout_user(request):
    logout(request)
