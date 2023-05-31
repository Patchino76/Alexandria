from django.http import HttpResponse

def say_shit(request):
    message = "Eat shits"
    return HttpResponse(message, content_type = 'plain/text')