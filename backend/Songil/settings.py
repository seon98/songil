# songil-django/backend/songil/settings.py
# (파일 상단에 environ 임포트)
import environ
import os
from pathlib import Path

# .env 파일 로드를 위한 설정
env = environ.Env(
    DEBUG=(bool, False)
)
BASE_DIR = Path(__file__).resolve().parent.parent
# .env 파일 경로 설정 (backend/.env)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# --- (기존 내용) ---
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
ALLOWED_HOSTS = ['*'] # 개발 중에는 모든 호스트 허용

# --- (수정/추가) Application definition ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # 1. GeoDjango(PostGIS) 앱 추가
    'django.contrib.gis',
    
    # 2. DRF 앱 추가
    'rest_framework',
    'rest_framework_gis', # DRF-GIS 추가
    
    # 3. 우리가 생성한 'tasks' 앱 추가
    'tasks.apps.TasksConfig',
    # 'users.apps.UsersConfig', # (나중에 users 앱 추가 시)
]
# --- (중간 생략) ---

# --- (수정) DATABASES ---
# Why: GeoDjango는 'django.contrib.gis' 엔진을 사용해야 합니다.
# How: django-environ의 env.db_url이 .env의 'postgis://'를
#      자동으로 파싱하여 아래 ENGINE을 포함한 딕셔너리로 만들어줍니다.
DATABASES = {
    'default': env.db_url('DATABASE_URL')
}

# --- (기타 설정) ---
LANGUAGE_CODE = 'ko-kr'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'