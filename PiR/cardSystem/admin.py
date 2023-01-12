from django.contrib import admin

# Register your models here.
from .models import Card, CardOwner

admin.site.register(Card)
admin.site.register(CardOwner)
