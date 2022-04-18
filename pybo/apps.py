from django.apps import AppConfig


class PyboConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pybo'

# 특별한 경우가 아니라면 PyboConfig 클래스를 수정할 일은 없다.