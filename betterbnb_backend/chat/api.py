from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer

@api_view(['GET'])
def conversation_list(request):
    """
    List all conversations.
    """
    conversations = request.user.conversations.all()
    if not conversations:
        return JsonResponse({'message': 'No conversations found.'}, status=404)
    serializer = ConversationListSerializer(conversations, many=True)
    return JsonResponse(serializer.data)