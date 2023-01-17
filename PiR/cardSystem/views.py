from django.shortcuts import render

# Create your views here.
from .models import Card


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_cards = Card.objects.all().count()

    context = {
        'num_cards': num_cards,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
