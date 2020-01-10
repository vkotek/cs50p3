from django.shortcuts import render

from .models import Item

# Create your views here.

def index(request):
    # return HttpResponse("Hello World!")
    context = {
        'menu': Item.objects.all()
    }
    return render(request, 'menu/index.html', context)