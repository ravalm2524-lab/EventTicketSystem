from django.db import models
from django.contrib.auth.models import User

# 1. Event Model (Event Ticket Details)
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True) 

    def __str__(self):
        return self.name

# 2. Booking Model (Ticket Transaction) - Ab sirf ek baar define kiya gaya hai
class Booking(models.Model):
    # Foreign Key: User (Kis user ne book kiya)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Foreign Key: Event (Kaunsa event book kiya)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # Booking ka samay (jo pehle joda gaya tha)
    booking_time = models.DateTimeField(auto_now_add=True)
    
    # --- YEH NAYA 'quantity' FIELD HAI ---
    quantity = models.IntegerField(default=1) 
    @property
    def total_price(self):
        return self.quantity * self.event.price
    def __str__(self):
        return f"Booking for {self.event.name} ({self.quantity} tickets) by {self.user.username}"