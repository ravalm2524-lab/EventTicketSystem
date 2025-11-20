from django.contrib import admin
from .models import Event, Booking

# Event Model ko register karein
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'price', 'is_active')
    list_filter = ('is_active', 'date')
    search_fields = ('name', 'location')
    ordering = ('date',)

## Booking Model ko register karein
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # list_display में 'quantity' और 'total_price_display' जोड़ दिया है
    list_display = ('id', 'event', 'user', 'quantity', 'booking_time', 'total_price_display')
    
    # Kis column se filter kar sakte hain
    list_filter = ('booking_time', 'event')
    
    # Search karne ki suvidha
    search_fields = ('user__username', 'event__name')
    
    # Latest bookings sabse pehle dikhao
    ordering = ('-booking_time',)
    
    # Sirf read-only fields
    readonly_fields = ('booking_time',) 

    # यह फंक्शन Admin Panel में Total Price दिखाएगा
    def total_price_display(self, obj):
        return f"₹{obj.total_price}"
    
    # कॉलम का नाम 'Total Price' रखने के लिए
    total_price_display.short_description = 'Total Price'   