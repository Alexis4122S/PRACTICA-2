from django.shortcuts import render

#create your views here.
def home(request):
    return render(request, 'notifications/index.html')

def notifications1(request):
    return render(request, 'notifications/list_notifications.html')