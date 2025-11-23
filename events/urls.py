from django.urls import path
from . import views
# Password Change ke liye yeh import zaroori hai
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Event Listing (Homepage)
    path('', views.event_list, name='event_list'),
    
    # 2. Event Detail & Booking
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/book/', views.book_event, name='book_event'),
    
    # 3. User Authentication (Login/Signup/Logout)
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # 4. My Tickets
    path('my_tickets/', views.my_tickets_view, name='my_tickets_view'),

    # 5. Profile Page
    path('profile/', views.profile_view, name='profile'),
    
    # 6. Change Password (Django Built-in Logic)
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='events/password_change.html',
        success_url='/profile/'
    ), name='password_change'),
    # ... baaki URLs ...
    
    # 7. Download PDF Ticket
    path('download-ticket/<int:booking_id>/', views.download_ticket, name='download_ticket'),
]