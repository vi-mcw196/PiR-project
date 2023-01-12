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
    card_owner = models.ForeignKey('CardOwner', on_delete=models.SET_NULL, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Card availability',
    )

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


class CardOwner(models.Model):
    """Model representing an CardOwner."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
