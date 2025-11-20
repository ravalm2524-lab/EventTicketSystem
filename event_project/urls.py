from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # यह लाइन आपके होमपेज ('/') और
    # ('/signup/', '/1/', '/1/book/') 
    # को 'events.urls' से जोड़ती है
    path('', include('events.urls')), 
]