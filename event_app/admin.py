from django.contrib import admin
from .models import Customer,EventDetails

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'mobile')


@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'event_city', 'guest_count')    


