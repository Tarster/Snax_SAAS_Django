from django.shortcuts import render
from base_app.scripts import script

# Create your views here.
def index(request):
    return render(request, 'base_app/index.html')

def script1(request):
    script.download_wikipedia_first_paragraph("Python_(programming_language)")
    return render(request, 'login/index.html')

def script2(request):    
    return render(request, 'base_app/script2.html')