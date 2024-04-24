from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Surveyor
from lands.models import Land
from django.core.exceptions import ObjectDoesNotExist
from .forms import SurveyorApplicationForm


@login_required
def surveyor_application(request):
    # Check if the user is already a surveyor
    if hasattr(request.user, 'surveyor'):
        return redirect('unconfirmed_lands')  # Redirect to survey land page if user is already a surveyor

    if request.method == 'POST':
        form = SurveyorApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            surveyor = form.save(commit=False)
            surveyor.user = request.user
            surveyor.save()
            return redirect('index')  # Redirect to home page after applying
    else:
        form = SurveyorApplicationForm()

    context = {
        'form': form
    }
    return render(request, 'surveyors/surveyor_application.html', context)

@login_required
def survey_land(request, land_id):
    # Get the land object or return a 404 error if not found
    land = get_object_or_404(Land, id=land_id)
    
    # Get the current user's surveyor profile
    surveyor = request.user.surveyor

    # Check if the surveyor is approved to survey lands
    if not surveyor.approved:
        # Redirect to a page indicating the surveyor is not approved
        return redirect('not_approved')

    if request.method == 'POST':
        # Get the user's selection from the form
        details_match = request.POST.get('details_match')

        # Update land's ownership status and confirmation status based on the user's selection
        if details_match == 'True':
            land.ownership_status = True
            land.confirmation_status = True
        else:
            land.ownership_status = False
            land.confirmation_status = False

        # Save the changes to the land
        land.save()
        return redirect('index')  # Redirect to the index page after surveying the land

    return render(request, 'surveyors/survey_land.html', {'land': land})


def not_approved(request):
    return render(request, 'surveyors/not_approved.html')
