from rest_framework import serializers
from .models import Conversation, ConversationMessage

from useraccount.serializers import UserDetailSerializer


class ConversationListSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'user', 'created_at', 'updated_at']

class ConversationDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['id', 'user', 'created_at', 'updated_at']

class ConversationMessageSerializer(serializers.ModelSerializer):
    sender = UserDetailSerializer(read_only=True, many=False)
    receiver = UserDetailSerializer(read_only=True, many=False)

    class Meta:
        model = ConversationMessage
        fields = ['id', 'conversation', 'body', 'sender', 'receiver', 'created_at']
