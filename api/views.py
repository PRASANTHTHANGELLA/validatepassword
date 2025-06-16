import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def validate_password(request):
    password = request.data.get('password')
    confirm_password = request.data.get('confirm_password')

    if not password or not confirm_password:
        return Response({'error': 'Both password and confirm_password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != confirm_password:
        return Response({'error': 'Passwords do not match.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(password) < 8:
        return Response({'error': 'Password must be at least 8 characters long.'}, status=status.HTTP_400_BAD_REQUEST)
    if not re.search(r'[A-Z]', password):
        return Response({'error': 'Password must contain at least one uppercase letter.'}, status=status.HTTP_400_BAD_REQUEST)
    if not re.search(r'\d', password):
        return Response({'error': 'Password must contain at least one number.'}, status=status.HTTP_400_BAD_REQUEST)
    if not re.search(r'[^A-Za-z0-9]', password):
        return Response({'error': 'Password must contain at least one special character.'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'Password is valid.'}, status=status.HTTP_200_OK)