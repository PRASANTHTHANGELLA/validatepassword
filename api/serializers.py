import re
from rest_framework import serializers

class PasswordValidationSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        if not password or not confirm_password:
            raise serializers.ValidationError('Both password and confirm_password are required.')

        if password != confirm_password:
            raise serializers.ValidationError('Passwords do not match.')

        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError('Password must contain at least one uppercase letter.')
        if not re.search(r'\d', password):
            raise serializers.ValidationError('Password must contain at least one number.')
        if not re.search(r'[^A-Za-z0-9]', password):
            raise serializers.ValidationError('Password must contain at least one special character.')

        return data