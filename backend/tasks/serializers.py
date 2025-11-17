# songil-django/backend/tasks/serializers.py
# Why: DRF-GIS의 Serializer를 사용하여 GeoJSON 형식으로 변환
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from .models import Task
# from django.contrib.gis.measure import D

class TaskSerializer(GeoFeatureModelSerializer):
    """
    '손길' 요청(Task)을 GeoJSON 피처로 직렬화합니다.
    (React의 Leaflet.js 라이브러리와 호환성이 좋습니다)
    """
    class Meta:
        model = Task
        # (중요) location 필드를 GeoJSON 'geometry'로 자동 변환
        geo_field = "location"
        # API 응답에 포함될 필드
        fields = ('id', 'title', 'description', 'reward', 'status', 'created_at')

class NearbyTaskSerializer(GeoFeatureModelSerializer):
    """
    주변 '손길' 요청 목록을 위한 시리얼라이저 (거리 포함)
    """
    # Why: View에서 annotate로 추가한 'distance' 값을 받기 위함
    distance = serializers.SerializerMethodField()

    class Meta:
        model = Task
        geo_field = "location"
        fields = ('id', 'title', 'reward', 'status', 'distance')

    def get_distance(self, obj):
        # obj에 'distance' 속성이 있는지 확인 (annotate로 주입됨)
        if hasattr(obj, 'distance'):
            # D 객체를 미터(m) 단위의 float으로 변환
            return round(obj.distance.m, 2)
        return None