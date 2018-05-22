from django.urls import include, path

from toys import views


urlpatterns = [
    path('toys/', views.toy_list, name='list'),
    path('toys/<pk>/', views.toy_detail, name='detail'),

]