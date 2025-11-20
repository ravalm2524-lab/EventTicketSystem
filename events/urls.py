from django.urls import path
from . import views

urlpatterns = [
    # 1. Event Listing (Homepage)
    path('', views.event_list, name='event_list'),
    
    # 2. Event Detail & Booking
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_event, name='book_event'),
    
    # 3. User Authentication
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # 4. My Tickets (Naya Path)
    path('my_tickets/', views.my_tickets_view, name='my_tickets_view'), # Nayi line
]