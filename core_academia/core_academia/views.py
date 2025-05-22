from django.shortcuts import render

def index(request):
    # Render the index.html template
    return render(request, 'index.html')
def about(request):
    # Render the about.html template
    return render(request, 'about.html')