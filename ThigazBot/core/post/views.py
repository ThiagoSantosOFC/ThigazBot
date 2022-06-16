from django.shortcuts import redirect, render

# Create your views here.

def index (request):
    if request.method == 'POST':
        content = request.get('content', '')
        
        if content:
            print("Content:", content)
            
            return redirect ('index')
        
    return render (request, 'post/index.html')