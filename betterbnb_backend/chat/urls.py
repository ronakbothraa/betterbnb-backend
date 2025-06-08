from django.urls import path

from . import api


urlpatterns = [
    path('', api.conversation_list, name='api_conversation_list'),
    path("start/<uuid:user_id>/", api.conversation_start, name='api_conversation_start'),
    path("<uuid:pk>/", api.conversation_detail, name='api_conversation_detail'),
]