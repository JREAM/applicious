from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from .models import Listings


def listings(request):
    """
    All Listings View
    """
    listings = Listings.objects.all()
    paginator = Paginator(listings, 10)

    page = request.GET.get('page')

    try:
        listings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        listings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        listings = paginator.page(paginator.num_pages)

    return render(request, 'listings.html', {'listings': listings})


def view(request, slug):
    pass


@login_required
def create(request):
    pass


@login_required
def edit(request, slug):
    pass


@login_required
def delete(request, slug):
    pass


@login_required
def pay(request, slug):
    pass
