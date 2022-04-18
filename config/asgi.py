"""
구성 프로젝트에 대한 ASGI 구성.

ASGI 콜러블을 ``application``이라는 모듈 수준 변수로 노출합니다.

이 파일에 대한 자세한 내용은 다음을 참조하십시오.
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_asgi_application()
