from django.shortcuts import render, get_object_or_404
from .models import Land
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def confirmed_lands(request):
    # Filter confirmed lands
    confirmed_lands = Land.objects.filter(confirmation_status=True)

    # Apply additional filters if provided
    location = request.GET.get('location')
    size = request.GET.get('size')
    price = request.GET.get('price')
    ownership_status = request.GET.get('ownership_status')
    owner = request.GET.get('owner')

    if location:
        confirmed_lands = confirmed_lands.filter(location__icontains=location)
    if size:
        confirmed_lands = confirmed_lands.filter(size=size)
    if price:
        confirmed_lands = confirmed_lands.filter(price=price)
    if ownership_status:
        confirmed_lands = confirmed_lands.filter(ownership_status=ownership_status)
    if owner:
        confirmed_lands = confirmed_lands.filter(owner__username=owner)

    # Pagination
    paginator = Paginator(confirmed_lands, 4)  # 4 lands per page
    page_number = request.GET.get('page')
    try:
        lands = paginator.page(page_number)
    except PageNotAnInteger:
        lands = paginator.page(1)
    except EmptyPage:
        lands = paginator.page(paginator.num_pages)

    context = {
        'lands': lands
    }
    return render(request, 'lands/confirmed_lands.html', context)

@login_required
def unconfirmed_lands(request):
    # Filter unconfirmed lands
    unconfirmed_lands = Land.objects.filter(confirmation_status=False)

    # Apply additional filters if provided
    location = request.GET.get('location')
    size = request.GET.get('size')
    price = request.GET.get('price')
    ownership_status = request.GET.get('ownership_status')
    owner = request.GET.get('owner')

    if location:
        unconfirmed_lands = unconfirmed_lands.filter(location__icontains=location)
    if size:
        unconfirmed_lands = unconfirmed_lands.filter(size=size)
    if price:
        unconfirmed_lands = unconfirmed_lands.filter(price=price)
    if ownership_status:
        unconfirmed_lands = unconfirmed_lands.filter(ownership_status=ownership_status)
    if owner:
        unconfirmed_lands = unconfirmed_lands.filter(owner__username=owner)

    # Pagination
    paginator = Paginator(unconfirmed_lands, 4)  # 4 lands per page
    page_number = request.GET.get('page')
    try:
        lands = paginator.page(page_number)
    except PageNotAnInteger:
        lands = paginator.page(1)
    except EmptyPage:
        lands = paginator.page(paginator.num_pages)

    context = {
        'lands': lands
    }
    return render(request, 'lands/unconfirmed_lands.html', context)

@login_required
def land_detail(request, land_id):
    land = get_object_or_404(Land, id=land_id)
    return render(request, 'lands/land_detail.html', {'land': land})

@login_required
def my_properties(request):
    # Get all lands owned by the current user
    my_lands = Land.objects.filter(owner=request.user)
    return render(request, 'lands/my_properties.html', {'my_lands': my_lands})
