from django.http import JsonResponse

def hello(request):
    return JsonResponse(data={"data": 123}, safe=False)
