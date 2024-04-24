from django.shortcuts import render
from .models import UserHistory, LandHistory
from django.contrib.auth.decorators import login_required

@login_required
def user_history(request):
    user_histories = UserHistory.objects.all()
    return render(request, 'history/user_history.html', {'user_histories': user_histories})

@login_required
def land_history(request):
    land_histories = LandHistory.objects.all()
    return render(request, 'history/land_history.html', {'land_histories': land_histories})
