# songil-django/backend/tasks/admin.py
# Why: Django 관리자 페이지에서 PostGIS 위치를 '지도'로 보기 위함
from django.contrib.gis import admin
from .models import Task


# How: 기본 admin.ModelAdmin 대신 OSMGeoAdmin (OpenStreetMap) 사용
@admin.register(Task)
class TaskAdmin(admin.GISModelAdmin):
    # 관리자 목록에 보여줄 필드
    list_display = ('title', 'status', 'reward', 'created_at')
    # 필터링 옵션
    list_filter = ('status',)
    # 검색 옵션
    search_fields = ('title', 'description')

    # (중요) location 필드를 OpenStreetMap으로 표시
    default_lon = 126.9780  # 서울 중심 경도
    default_lat = 37.5665  # 서울 중심 위도
    default_zoom = 11