from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User




def get_string(request):
    # Chuỗi bạn muốn trả về
    response_string = "Hello, this is a string response from Django API!"
    
    # Trả về một JsonResponse với chuỗi
    return JsonResponse({'message': response_string})



def get_user_list(request):
    # Chuỗi bạn muốn trả về
    users=User.objects.all().values('id', 'first_name','last_name', 'email')
    user_list = list(users)    
    # Trả về một JsonResponse với chuỗi
    return JsonResponse({'list': user_list})

