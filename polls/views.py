from django.http import HttpResponse

def polls(request):
    return HttpResponse("hello world. at the polls")
# Create your views here.
