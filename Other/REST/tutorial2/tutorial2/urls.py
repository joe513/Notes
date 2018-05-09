from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include(('snippets.urls', 'snippets'))),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
