from django.shortcuts import render

# Create your views here.
from .models import Card, CardOwner


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cards = Card.objects.all().count()
    num_owners = CardOwner.objects.all().count()

    # Available books (status = 'a')
    num_cards_available = Card.objects.filter(status__exact='a').count()

    context = {
        'num_cards': num_cards,
        'num_owners': num_owners,
        'num_cards_available': num_cards_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
