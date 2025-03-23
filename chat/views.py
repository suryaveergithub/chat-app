from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def sender(request, room_name, username):
    return render(request, 'chat/sender.html', {
        'room_name': room_name,
        'username': username
    })

def receiver(request, room_name, username):
    return render(request, 'chat/receiver.html', {
        'room_name': room_name,
        'username': username
    })
