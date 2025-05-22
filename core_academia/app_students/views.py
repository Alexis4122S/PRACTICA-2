from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'students/index.html')
def list_students1(request):
    return render(request, 'students/list_students.html')