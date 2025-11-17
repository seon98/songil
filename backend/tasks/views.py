# songil-django/backend/tasks/views.py
from rest_framework.generics import ListAPIView
from .models import Task
from .serializers import NearbyTaskSerializer

# GeoDjango 임포트
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D  # 'Distance' 객체
from django.contrib.gis.db.models.functions import Distance


class NearbyTaskListView(ListAPIView):
    """
    GET /api/v1/tasks/nearby/
    주변 1km(기본) 이내의 '손길' 요청을 가까운 순으로 반환합니다.

    Query Params:
    - lat (float): 헬퍼의 현재 위도 (필수)
    - lon (float): 헬퍼의 현재 경도 (필수)
    - radius_m (int): 검색 반경(m) (기본: 1000)
    """
    serializer_class = NearbyTaskSerializer

    def get_queryset(self):
        # 1. 쿼리 파라미터에서 위도/경도/반경 추출
        try:
            latitude = float(self.request.query_params.get('lat'))
            longitude = float(self.request.query_params.get('lon'))
            radius_meters = int(self.request.query_params.get('radius_m', 1000))
        except (TypeError, ValueError):
            # 필수 파라미터가 없으면 빈 쿼리셋 반환
            return Task.objects.none()

        # 2. 헬퍼의 현재 위치를 GeoDjango Point 객체로 생성 (SRID 4326)
        # (주의: Point 생성자는 (경도, 위도) 순서입니다)
        helper_location = Point(longitude, latitude, srid=4326)

        # 3. GeoDjango 쿼리 실행
        # Why:
        # 1. location__dwithin: PostGIS의 ST_DWithin을 사용하여
        #    'helper_location'으로부터 'radius_meters' 거리 내의 Task만 필터링 (인덱스 사용)
        # 2. annotate(distance=...): ST_Distance를 사용하여
        #    각 Task와 헬퍼 간의 실제 거리를 'distance' 필드로 추가
        # 3. order_by('distance'): 계산된 거리 순으로 정렬

        queryset = Task.objects.filter(
            status='PENDING',
            location__dwithin=(helper_location, D(m=radius_meters))
        ).annotate(
            distance=Distance('location', helper_location)
        ).order_by('distance')

        return queryset