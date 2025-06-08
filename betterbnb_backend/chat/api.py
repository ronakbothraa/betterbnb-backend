from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import Conversation
from useraccount.models import User
from .serializers import ConversationListSerializer, ConversationDetailSerializer, ConversationMessageSerializer

@api_view(['GET'])
def conversation_list(request):
    """
    List all conversations.
    """
    conversations = request.user.conversations.all()
    serializer = ConversationListSerializer(conversations, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    conversation_serializer = ConversationDetailSerializer(conversation, many=False)
    message_serializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

    return JsonResponse({
        'conversation': conversation_serializer.data,
        'messages': message_serializer.data
    }, safe=False)


@api_view(['Get'])
def conversation_start(request, user_id):
    conversation = Conversation.objects.filter(user__in=[request.user.id]).filter(user__in=[user_id]).first()
    if conversation:
        return JsonResponse({'conversation_id': conversation.id}, status=200)
    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.user.add(request.user)
        conversation.user.add(user)
        return JsonResponse({'conversation_id': conversation.id}, status=201)