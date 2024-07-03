# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('', include('members.urls')),
#     path('admin/', admin.site.urls),
# ]# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/get-string/', views.get_string, name='get_string_api'),
]

# urlpatterns = [
#     path('api/user/', views., name='get_string_api'),
# ]

urlpatterns = [
    path('api/get-users/', views.get_user_list, name='get_user_list_api'),
]