from rest_framework import serializers
from .models import Like
from django.db.models import F

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = ['user', 'quantity']
        read_only_fields = ['user', 'quantity']

    def create(self, validated_data):
        user = self.context['request'].user
        like = Like.objects.get_or_create(user=user)[0]
        like.quantity += 1
        like.save()
        return like