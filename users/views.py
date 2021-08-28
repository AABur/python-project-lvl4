from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import User

# Create your views here.


def nickname(request, user_id):
    response = "You're looking at the nickname of user %s."
    return HttpResponse(response % user_id)


def full_name(request, user_id):
    return HttpResponse("Full_name of user %s." % user_id)


def index(request):
    latest_user_list = User.objects.order_by('-registarration_date')[:5]
    context = {'latest_user_list': latest_user_list}
    return render(request, 'users/index.html', context)


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})
