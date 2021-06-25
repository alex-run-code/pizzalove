from rest_framework import serializers
from .models import Like
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ['user', 'quantity']
        read_only_fields = ['user', 'quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        if Like.objects.filter(user=user).exists():
            Like.objects.filter(user=user).update(quantity=F('quantity')+1)
        else:
            Like.objects.create(user=user, quantity=1)
        return Like.objects.get(user=user)