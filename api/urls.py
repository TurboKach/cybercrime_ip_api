from django.urls import path

from .views import get_ips, get_lists, update_lists

urlpatterns = {
    path('ip', get_ips, name="get_ips"),
    path('list', get_lists, name="get_lists"),
    path('management/update', update_lists, name='update_lists')
}