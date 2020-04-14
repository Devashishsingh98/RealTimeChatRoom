from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    error = False
    
    if request.user.is_authenticated:
        print("Dont fuck wid me bro. You already joined!")

    if request.method == "POST":
        username = request.POST["username"]
        room_name = request.POST["room_name"]
        
        if username not in list(map(str, User.objects.all())):
            new_user = User(username=username)
            new_user.save()
            login(request, new_user)
            return redirect(room, room_name=room_name)
        else:
            error = True

    return render(request, "chat/index.html", {"error":error})

@login_required
def room(request, room_name):
    return render(request, "chat/room.html", {
        "room_name":room_name,
        "username":request.user.username
        })
