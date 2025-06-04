from django.http import JsonResponse
from rest_framework.decorators import api_view


from .serializers import ConversationListSerializer

@api_view(['GET'])
def conversation_list(request):
    """
    List all conversations.
    """
    conversations = request.user.conversations.all()
    serializer = ConversationListSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)