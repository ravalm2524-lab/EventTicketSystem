from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Booking
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# 1. होमपेज (सभी इवेंट्स)
# (इसके ऊपर @login_required नहीं है)
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# 2. डिटेल पेज (यह फंक्शन आपके कोड से गायब हो गया था)
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

# events/views.py mein book_event function ko badlein
# ...

@login_required
def book_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        try:
            # 1. Quantity ko integer mein badalte hain
            ticket_quantity = int(request.POST.get('quantity', 1))
            if ticket_quantity <= 0:
                ticket_quantity = 1
        except ValueError:
            ticket_quantity = 1
            
        # 2. Total Price ki ganana karte hain (Maana ki Event model mein 'price' field hai)
        # Agar aapka price float ya Decimal field hai, to ye calculation sahi hogi.
        total_price = event.price * ticket_quantity
        
        # 3. New Booking banate hain
        new_booking = Booking(
            event=event, 
            user=request.user, 
            quantity=ticket_quantity
        )
        new_booking.save()
        
        # 4. Confirmation page par bhejein (ab Total Price bhi bhej rahe hain)
        context = {
            'event': event, 
            'quantity': ticket_quantity, 
            'total_price': total_price # <--- Naya Data
        }
        return render(request, 'events/booking_confirmation.html', context)
    
    return redirect('event_detail', event_id=event.id)
# 4. साइन-अप व्यू
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

# 5. लॉग-इन व्यू
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                
                # यूज़र को 'next' पेज पर भेजें (अगर वह मौजूद है)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect('event_list')
    else:
        form = AuthenticationForm()
    return render(request, 'events/login.html', {'form': form})

# 6. लॉग-आउट व्यू
def logout_view(request):
    logout(request)
    return redirect('event_list')
# events/views.py mein sabse neeche yeh function jod dein:

# events/views.py

# ... (बाकी import statements और functions) ...

# events/views.py

@login_required
def my_tickets_view(request):
    # 1. डेटाबेस से बुकिंग लाएं
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
    
    # ❌ पुरानी कैलकुलेशन वाला लूप यहाँ से हटा दें (Delete old loop)
    # Model अपने आप total_price कैलकुलेट कर लेगा।

    # 2. सीधे टेंप्लेट को भेज दें
    return render(request, 'events/my_tickets.html', {'bookings': bookings})
    # User Profile View
@login_required
def profile_view(request):
    return render(request, 'events/profile.html')