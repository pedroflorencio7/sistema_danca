from django.urls import path
from starter.views import index

app_name = 'starter'

urlpatterns = [
    path('', index, name='index')
]