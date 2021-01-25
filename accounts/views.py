from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils import timezone
from .models import userImage
from events.models import events


def home(request):
    return render(request, 'accounts/home.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error':'Username or Password Does Not Match!'})
    else:
        return render (request, 'accounts/login.html')

def signup(request):
    if request.method =="POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['email'])
                return render(request, 'accounts/login.html', {'error':'Email Address Already exists!'})
            
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'], first_name=request.POST['username'])
                auth.login(request, user)
                return redirect('confirmed')
        else:
            return render(request, 'accounts/login.html', {'error':'Passwords Do Not Match!'})
    else:
        return render (request, 'accounts/login.html')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

def confirmed(request):
    return render(request, 'accounts/signupconformation.html')

def account(request):
    User = request.user
    userimgs = userImage.objects.all()
    event = events.objects.all()
    if User.username == "beowulfadmin@gmail.com":
        return render(request, 'accounts/adminaccount.html', context={'userimg': userimgs, 'events':event})
    else:
        usrimgs = userImage.objects.filter(user=User)
        return render(request, 'accounts/account.html', {'userimg': usrimgs})

def add_event(request):
    add_event = events.objects.all()
    if request.method =='POST':
        if request.POST['title'] and request.POST['date'] and request.POST['time'] and request.POST['description']:
            event = events()
            event.title = request.POST['title']
            event.date = request.POST['date']
            event.time = request.POST['time']
            event.description = request.POST['description']
            event.save()
            return redirect('account')
        else:
            return render(request,'accounts/adminaccount.html', {'error':'All Fields Are Required'})
    else:
        return render(request,'accounts/adminaccount.html')

def deleteEvent(request, events_id):
    event = events.objects.all()
    if request.method =='POST':
        delevent = get_object_or_404(events, pk=events_id)
        delevent.delete()
        return redirect('account')
    else:
        return render(request,'accounts/adminaccount.html', {'event':event})

def updateimage(request, userImage_id):
    User = request.user
    usrimgs = userImage.objects.filter(user=User)
    if request.method == "POST":
        images =  get_object_or_404(userImage, pk=userImage_id)
        images.profilePic = request.FILES['image']
        images.user = request.user
        images.save()
        return render(request, 'accounts/account.html', {'userimg': usrimgs})