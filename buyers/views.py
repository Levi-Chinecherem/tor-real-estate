from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Buyer
from lands.models import Land
from .forms import BuyerAgreementForm


@login_required
def buyer_application(request):
    # Check if the user is already a buyer
    if hasattr(request.user, 'buyer') and request.user.buyer:
        return redirect('confirmed_lands')  # Redirect to home page if user is already a buyer

    if request.method == 'POST':
        form = BuyerAgreementForm(request.POST)
        if form.is_valid():
            buyer = form.save(commit=False)
            buyer.user = request.user
            buyer.save()
            return redirect('confirmed_lands')  # Redirect to home page after signing agreement
    else:
        form = BuyerAgreementForm()
    
    return render(request, 'buyers/buyer_application.html', {'form': form})

@login_required
def buy_land(request, land_id):
    land = get_object_or_404(Land, id=land_id)

    if request.method == 'POST':
        # Update the land's owner to the current user
        land.owner = request.user
        land.save()
        return redirect('my_properties')  # Redirect to the index page after buying the land

    return render(request, 'buyers/buy_land.html', {'land': land})
