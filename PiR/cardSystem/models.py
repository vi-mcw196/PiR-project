import uuid

from django.db import models
from django.urls import reverse


class Card(models.Model):
    """Class Card"""

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular card across whole cardSystem')
    card_number = models.CharField(max_length=20, help_text='Enter card number')
    date_of_last_use = models.DateField(null=True, blank=True, auto_now_add=True)
    card_owner = models.CharField(max_length=20, help_text='Enter name and surname of the owner')

    # Metadata
    class Meta:
        ordering = ['-date_of_last_use']

    # Methods
    def get_absolute_url(self):
        """Returns the URL to access a particular instance of MyModelName."""
        return reverse('card-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f'{self.card_number} ({self.card_owner})'
