from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def base_layout(request):
    template = 'itinerary_app/home.html'
    return render(request, template)

def result(request):
    return render(request, 'result.html')


@login_required
def itin(request):
    return render(request, 'itinerary_app/form.html')
