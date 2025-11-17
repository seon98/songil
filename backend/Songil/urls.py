# songil-django/backend/songil/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Why: React와 통신할 API 엔드포인트
    # How: /api/v1/tasks/ 로 오는 모든 요청을 'tasks.urls'로 위임
    path('api/v1/tasks/', include('tasks.urls')),
    # path('api/v1/users/', include('users.urls')), # (나중에 추가)
]