from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .serializers import UserDetailSerializer
from .models import User


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def host_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    serializer = UserDetailSerializer(user)
    return JsonResponse(serializer.data, safe=False)