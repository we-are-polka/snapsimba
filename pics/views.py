from django.shortcuts import render
from .models import Picha

# Create your views here.
def homepage(request):
    all_images = Picha.objects.all()
    return render(request, 'index.html', {'all_images':all_images})