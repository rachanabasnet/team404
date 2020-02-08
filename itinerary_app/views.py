from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

# <<<<<<< HEAD
# def result(request):
#     return render(request, 'result.html')
# =======


def itin(request):
    return render(request, 'form.html')
# >>>>>>> 684cd8b0a641e028910bd158ff019ed727b8ce38
