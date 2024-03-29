from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


class SimpleRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['title', 'artist', 'year', ]
