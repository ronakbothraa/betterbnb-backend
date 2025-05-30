from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import PropertyForm
from .models import Property, Reservation
from .serializers import PropertiesListSerializer, PropertyDetailSerializer, PropertyReservationSerializer


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)
    return JsonResponse({
        "data": serializer.data,
    })



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def property_detail(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)

    serializer = PropertyDetailSerializer(property)
    return JsonResponse({
        "data": serializer.data,
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def property_reservation_detail(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return JsonResponse({"error": "Property not found"}, status=404)

    serializer = PropertyReservationSerializer(property.reservations.all(), many=True)
    return JsonResponse({
        "data": serializer.data,
    })


@api_view(['POST'])
def create_property(request):
    form = PropertyForm(request.POST, request.FILES)
    if form.is_valid():
        property = form.save(commit=False)
        property.host = request.user
        property.save()
        return JsonResponse({"success": True, "property_id": property.id})
    else:
        print("Form errors:", form.errors, form.non_field_errors)
        return JsonResponse({"success": False, "errors": form.errors.as_json()}, status=400)

@api_view(['POST'])
def book_property(request, pk):
    try: 
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        guests = request.POST.get("guests", 1)
        total_price = request.POST.get("total_price")

        property = Property.objects.get(pk=pk)
        created_by = request.user

        reservation = Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            guests=guests,
            total_price=total_price,
            created_by=created_by
        )
        
        return JsonResponse({"success": True, "reservation_id": reservation.id})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)