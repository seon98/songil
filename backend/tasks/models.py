# songil-django/backend/tasks/models.py
# Why: Django ORM 대신 GeoDjango의 models를 사용
from django.contrib.gis.db import models


# from django.conf import settings # (나중에 User 모델 연결 시)

class Task(models.Model):
    """
    '손길' 요청(Task) 모델
    """
    # (Django는 id 필드를 자동으로 생성합니다)
    title = models.CharField(max_length=255, verbose_name="요청 제목")
    description = models.TextField(blank=True, verbose_name="요청 내용")
    reward = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="보상(비용)")

    # Why: GeoDjango의 PointField 사용. PostGIS의 Point 타입과 매핑됨.
    #      srid=4326은 표준 GPS 위도/경도(WGS84)를 의미.
    location = models.PointField(srid=4326, verbose_name="수행 위치")

    # (Enum은 Django 4.x 이상에서는 models.TextChoices 사용 가능)
    STATUS_CHOICES = [
        ('PENDING', '매칭 대기 중'),
        ('MATCHED', '매칭됨'),
        ('IN_PROGRESS', '수행 중'),
        ('COMPLETED', '완료됨'),
        ('CANCELLED', '취소됨'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING',
        db_index=True  # 상태별 검색을 위해 인덱스 추가
    )

    # TODO: User 모델 완성 후 ForeignKey 연결
    # requester = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     related_name='requested_tasks'
    # )
    # helper = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True, blank=True,
    #     related_name='helped_tasks'
    # )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title