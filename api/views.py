from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PasswordValidationSerializer

@api_view(['POST'])
def validate_password(request):
    serializer = PasswordValidationSerializer(data=request.data)
    if serializer.is_valid():
        return Response({'message': 'Password is valid.'}, status=status.HTTP_200_OK)
    return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)