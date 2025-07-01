from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_info, name='customer_info'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('select-event/', views.select_event, name='select_event'),
    path('event-details/', views.event_details, name='event_details'),  # ✅ fixed here
    path('final-form/', views.final_form, name='final_form'),
    path('show-services/', views.show_services, name='show_services'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('date-time-slot/', views.date_time_slot, name='date_time_slot'),
]
