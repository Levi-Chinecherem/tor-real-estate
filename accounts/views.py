from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from history.models import UserHistory, Role
from lands.models import Land
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def custom_error_view(request, exception=None):
    error_code = 500 if exception is None else 404
    error_message = "Internal Server Error" if exception is None else "Page Not Found"

    context = {
        'error_code': error_code,
        'error_message': error_message
    }
    return render(request, 'error.html', context)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the index page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the index page after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required  # Require user to be logged in to access this view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout

@login_required  # Require user to be logged in to access this view
def password_change_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the index page after successful password change
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/password_change.html', {'form': form})


@login_required
def profile_view(request, user_id=None):
    if user_id:
        # If user_id is provided, show the profile of that user
        user = User.objects.get(pk=user_id)
        user_history, _ = UserHistory.objects.get_or_create(user=user)
    else:
        # If no user_id is provided, show the logged-in user's profile
        user = request.user
        user_history, _ = UserHistory.objects.get_or_create(user=user)

    # Get the roles of the user
    roles = user_history.roles.all()

    # Check if user is a seller, buyer, or surveyor
    is_seller = roles.filter(name='Seller').exists()
    is_buyer = roles.filter(name='Buyer').exists()
    is_surveyor = roles.filter(name='Surveyor').exists()

    # Initialize document details
    agreement_details = None

    # Get details from agreement document if user is a seller
    if is_seller:
        # Get the latest land uploaded by the user
        latest_land = Land.objects.filter(owner=user).order_by('-owner').first()
        if latest_land:
            agreement_details = {
                'land': latest_land,
                'owner': latest_land.owner,
                'status': latest_land.status,
            }

    context = {
        'user': user,
        'is_seller': is_seller,
        'is_buyer': is_buyer,
        'is_surveyor': is_surveyor,
        'agreement_details': agreement_details,
    }

    return render(request, 'accounts/profile.html', context)
