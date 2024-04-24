# views.py in the Sellers app

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Seller
from .forms import SellerAgreementForm, LandUploadForm
from lands.models import Land

@login_required
def seller_application(request):
    # Check if the user is already a seller
    if hasattr(request.user, 'seller'):
        return redirect('land_upload')  # Redirect to home page if user is already a seller

    if request.method == 'POST':
        form = SellerAgreementForm(request.POST, request.FILES)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.user = request.user
            seller.agreement_accepted = True
            seller.save()
            return redirect('land_upload')  # Redirect to land upload page after signing agreement
    else:
        form = SellerAgreementForm()
    
    return render(request, 'sellers/seller_application.html', {'form': form})


@login_required
def land_upload(request):
    # Check if the user has signed the seller agreement
    if not request.user.seller:
        return redirect('seller_application')  # Redirect to seller application if not a seller

    if request.method == 'POST':
        form = LandUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Exclude ownership_status and confirmation_status from form data
            new_land = form.save(commit=False)
            new_land.owner = request.user  # Assign the current user as the owner
            new_land.save()
            return redirect('unconfirmed_lands')  # Redirect to home page or wherever you want
    else:
        form = LandUploadForm()

    context = {
        'form': form
    }
    return render(request, 'sellers/land_upload.html', context)
