from django.urls import path
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    path('schema/', schema_view),

]
