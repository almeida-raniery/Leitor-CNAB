from rest_framework import serializers

def validate_numeric(value):
    if not value.isdigit():
      raise serializers.ValidationError("This field must be numeric")