from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'error_app/404.html', status=404)
