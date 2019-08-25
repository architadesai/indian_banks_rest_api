from rest_framework import serializers
from .models import Branches


class BranchesBankSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='bank.name')

    class Meta:
        model = Branches
        fields = ("ifsc", "name", "branch", "address", "city", "district", "state")
