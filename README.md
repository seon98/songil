# 🚀 손길 (Songil) - Django 백엔드



> '손길' 하이퍼로컬 C2C 매칭 플랫폼 (Django + React 풀스택)

이 저장소는 '손길' 서비스의 풀스택 코드를 관리하는 모노레포입니다.

## 📚 핵심 기술 스택 (Open Source)

* **Backend:** **Python / Django / Django Rest Framework (DRF)**
    * 'Batteries-included' 프레임워크로 빠른 개발.
* **Database:** **PostgreSQL + PostGIS (GeoDjango)**
    * `GeoDjango` (`django.contrib.gis`)를 통한 네이티브 지리 공간 쿼리 지원.
* **Infra & DevOps:** **Docker**
    * `GDAL` 등 복잡한 시스템 의존성을 Docker로 완벽하게 격리.

## ⚙️ 개발 환경 실행 (macOS/Linux 기준)

이 프로젝트는 Docker Compose를 사용하여 백엔드와 데이터베이스를 실행합니다.

1.  **Docker 실행:**
    (Docker Desktop이 실행 중이어야 합니다.)
    ```bash
    # (루트 'songil-django' 디렉터리에서 실행)
    docker-compose up -d --build
    ```

2.  **(최초 1회) Django 프로젝트 생성:**
    `docker-compose`가 실행 중인 상태에서, 별도 터미널에서 다음을 실행하여 Django 프로젝트와 앱의 뼈대를 생성합니다.
    ```bash
    # Django 'songil' 프로젝트 생성 (현재 디렉터리에)
    docker-compose run --rm backend django-admin startproject songil .
    
    # 'tasks' 앱 생성
    docker-compose run --rm backend python manage.py startapp tasks
    ```
    *(이후 이 명령어들은 다시 실행할 필요 없습니다.)*

3.  **(최초 1회) 데이터베이스 마이그레이션:**
    모델(models.py)이 DB에 적용되도록 마이그레이션을 실행합니다.
    ```bash
    docker-compose exec backend python manage.py migrate
    ```

4.  **API 확인:**
    * `http://localhost:8000/api/v1/tasks/nearby/?lat=...&lon=...`
    * `http://localhost:8000/admin/` (관리자 페이지)

5.  **(선택) Superuser 생성:**
    `/admin` 페이지에 접속하기 위한 관리자 계정을 생성합니다.
    ```bash
    docker-compose exec backend python manage.py createsuperuser
    ```