from django.shortcuts import render
from .models import events

def viewEvents(request):
    event = events.objects.all().order_by('-id')
    return render(request, 'events/events.html', {'events':event})
