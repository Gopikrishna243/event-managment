from django.shortcuts import render, redirect
from .models import Customer,EventDetails

from django.shortcuts import render, redirect

def customer_info(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        city = request.POST.get('city')
        mobile = request.POST.get('mobile')

        Customer.objects.create(name=name, city=city, mobile=mobile)

        request.session['name'] = name
        request.session['city'] = city
        request.session['mobile'] = mobile

        return redirect('select_event')  
    
    return render(request, 'customer_info.html')



def thank_you(request):
    return render(request, 'thank_you.html')


def select_event(request):
    if request.method == 'POST':
        request.session['event_type'] = request.POST.get('event_type')
        return redirect('event_details')  # Use the actual name in your `urls.py`

    events = [
        {"name": "Marriage", "image": "images/marriage.png"},
        {"name": "Birthday", "image": "images/birthday.png"},
        {"name": "Cradle Ceremony", "image": "images/credle.png"},
        {"name": "Death Day", "image": "images/death.png"},
    ]
    
    return render(request, 'select_event.html', {'events': events})


def event_details(request):
    if request.method == 'POST':
        event_city = request.POST.get('event_city')
        guest_count = request.POST.get('guest_count')
        manage_type = request.POST.get('manage_type')

        # Save to session
        request.session['event_city'] = event_city
        request.session['guest_count'] = guest_count
        request.session['manage_type'] = manage_type

        # DEBUG PRINT
        print("Manage Type:", manage_type)

        if manage_type.strip() == "Event is on us":
            return redirect('final_form')  # should redirect correctly now
        else:
            return redirect('show_services')  # otherwise go to services

    return render(request, 'event_details.html')


from django.shortcuts import render, redirect

from datetime import date, timedelta

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import EventDetails  # Ensure your model is named exactly this

def final_form(request):
    event_type = request.session.get('event_type')
    event_city = request.session.get('event_city')
    guest_count = request.session.get('guest_count')
    manage_type = request.session.get('manage_type')

    min_date = (timezone.now().date() + timedelta(days=2)).isoformat()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        area = request.POST.get('area')
        preferred_date = request.POST.get('date')
        preferred_time = request.POST.get('time')

        # Save to database
        EventDetails.objects.create(
            name=name,
            email=email,
            contact=contact,
            area=area,
            event_type=event_type,
            event_city=event_city,
            guest_count=guest_count,
        )

        return render(request, 'confirmation.html', {
            'name': name,
            'event_type': event_type,
            'event_city': event_city,
            'guest_count': guest_count,
            'area': area,
            'preferred_date': preferred_date,
            'preferred_time': preferred_time
        })

    return render(request, 'final_form.html', {'min_date': min_date})




def show_services(request):
    services = {
        "Gurus": [
            {"name": "Pandit Sharma", "area": "Hyderabad", "phone": "9876543210"},
            {"name": "Pandit Joshi", "area": "Secunderabad", "phone": "9876500000"},
        ],
        "Caterers": [
            {"name": "Sai Caterers", "area": "Hyderabad", "phone": "9876123456"},
            {"name": "Sri Annapurna", "area": "Kukatpally", "phone": "9876987654"},
        ],
        "Venues": [
            {"name": "Sri Lakshmi Hall", "area": "Ameerpet", "phone": "9876112233"},
            {"name": "Kalyana Mandapam", "area": "Miyapur", "phone": "9876009988"},
        ],
    }
    return render(request, 'show_services.html', {'services': services})


from datetime import date, timedelta

def date_time_slot(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        selected_time = request.POST.get('time_slot')

        # Store in session or DB as needed
        request.session['selected_date'] = selected_date
        request.session['selected_time'] = selected_time

        return redirect('confirmation')

    min_date = date.today() + timedelta(days=2)
    return render(request, 'date_time_slot.html', {
        'min_date': min_date.strftime('%Y-%m-%d')
    })


def confirmation(request):
    name = request.session.get('name')
    event_type = request.session.get('event_type')
    event_city = request.session.get('event_city')
    guest_count = request.session.get('guest_count')
    area = request.session.get('area')
    selected_date = request.session.get('selected_date')
    selected_time = request.session.get('selected_time')

    return render(request, 'confirmation.html', {
        'name': name,
        'event_type': event_type,
        'event_city': event_city,
        'guest_count': guest_count,
        'area': area,
        'selected_date': selected_date,
        'selected_time': selected_time
    })


