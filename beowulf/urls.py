
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts import views as account_views
from accounts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.home, name='home'),
    #accounts
    path('accounts/', include('accounts.urls')),
    #crusade
    #find
    path('location/', include('findus.urls')),
    #events
    path('event/', include('events.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
