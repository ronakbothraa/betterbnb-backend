from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from property.serializers import PropertyReservationSerializer

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

@api_view(['GET'])
def reservations_list(request):
    reservations = request.user.reservations.all()
    serializer = PropertyReservationSerializer(reservations, many=True)

    return JsonResponse(serializer.data, safe=False)