from django.shortcuts import render

# Create your views here.
def error(request):
    if request.method == 'GET':
        return render(request, 'errors/error.html', context={'message':request.GET["er"]}) 

def generic_error(request):
    if request.method == 'GET':
        return render(request, 'errors/generic.html', context={}) 