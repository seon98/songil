# songil-django/backend/Dockerfile
FROM python:3.11-slim

# Timezone 설정 (선택 사항)
ENV TZ=Asia/Seoul
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Why: GeoDjango에 필수적인 GDAL 라이브러리 설치
# How: apt-get(Debian 패키지 관리자)을 사용하여 시스템 레벨에 설치
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       gdal-bin \
       libgdal-dev \
       python3-gdal \
       # psycopg2 컴파일에 필요한 build-essential, libpq-dev
       build-essential \
       libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# requirements.txt를 먼저 복사하여 Docker 캐시 활용
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 나머지 코드 복사 (manage.py, songil/, tasks/ 등)
# (주의: 이 파일들은 'docker-compose run'으로 생성한 이후에 복사됩니다)
COPY . .