
from rest_framework import serializers
from . models import Items

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Items
        fields='__all__'