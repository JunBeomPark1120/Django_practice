from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    
    username = '박준범'
    
    result = {
        'username' : username,
    }
    
    return render(request, 'hello.html', result)