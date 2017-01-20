from django.http import HttpResponse

def index(request):
    return HttpResponse("DOH says hey there partner!")