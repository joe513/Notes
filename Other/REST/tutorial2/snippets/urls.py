from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippets'

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='list'),
    path('snippets/<pk>/', views.SnippetDetail.as_view(), name='detail'),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<pk>', views.UserDetail.as_view(), name='user')
]

urlpatterns = format_suffix_patterns(urlpatterns)
