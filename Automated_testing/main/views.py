# views.py
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            return JsonResponse({'msg': 'Login Success'})
        return JsonResponse({'msg': 'Invalid credentials'}, status=401)
    return JsonResponse({'msg': 'Only POST allowed'}, status=405)
