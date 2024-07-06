from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello_recruto(request):
    name = request.GET.get('name', 'Recruto')
    message = request.GET.get('message', 'Давай дружить')
    response_text = f"Hello {name}! {message}!"
    return HttpResponse(response_text)
