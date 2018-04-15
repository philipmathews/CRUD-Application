from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404

from django.http import HttpResponse, HttpResponseRedirect

from .models import Users, Events

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login, authenticate,logout

from django.contrib.auth.decorators import login_required

from .forms import UserLoginForm, EventForm

from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        return redirect('app1:dashboard')
    
    return render(request, 'app1/home.html')

def log_in(request):
    if request.user.is_authenticated:
        return redirect('app1:dashboard')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('app1:dashboard')
            else:
                return render(request,'registration/login.html',{'form' : form,'user' : user})
    else:
        form = UserLoginForm
    context = { 'form' : form }
    return render(request,'registration/login.html', context)


def log_out(request):
    logout(request)
    return redirect('app1:home')



def register(request):
    if request.user.is_authenticated:
        return redirect('app1:dashboard')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            u = User.objects.get(username=username)
            if u is not None:
                c = Users(username=username)
                c.save()
            return redirect('app1:dashboard')
    else:
        form = UserCreationForm()

    context = { 'form' : form }
    return render(request, 'registration/register.html', context)

@login_required(login_url='/login')
def dashboard(request):
    username = request.user
    userkey= get_object_or_404(Users, username= username)
    context = {'userkey' : userkey }
    return render(request, 'app1/dashboard.html',context)

@login_required(login_url='/login')
def create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            userkey = request.user
            username = get_object_or_404(Users, username=userkey)
            event = username.events_set.create(title=request.POST['title'],description = request.POST['description'],location = request.POST['location'],date = request.POST['date'],attended_or_not = request.POST['attended_or_not'])
            return redirect('app1:dashboard')
    else:
        form = EventForm()

    context = { 'form' : form }
    return render(request,'app1/create.html', context)

@login_required(login_url='/login')
def edit(request,id):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = get_object_or_404(Events,pk=id)
            event.title = request.POST['title']
            event.description = request.POST['description']
            event.location = request.POST['location']
            event.date = request.POST['date']
            event.attended_or_not = request.POST['attended_or_not']
            event.save()
            return redirect('app1:dashboard')
    else:
        event = get_object_or_404(Events,pk=id)
        data={'title' : event.title,
       'description' : event.description,
       'location' : event.location,
       'date' : event.date,
       'attended_or_not' : event.attended_or_not}
        form = EventForm(data)

    context = { 'form' : form, 'event' : event }
    return render(request,'app1/edit.html', context)

@login_required(login_url='/login')
def delete(request,id):
    event = get_object_or_404(Events,pk=id)
    event.delete()
    return redirect('app1:dashboard')



