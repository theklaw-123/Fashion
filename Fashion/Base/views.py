from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Base/dashboard.html')

def Products(request):
    return render(request, 'Base/products.html')