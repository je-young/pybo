#!/usr/bin/env python
"""관리 작업을 위한 Django의 명령줄 유틸리티."""
import os
import sys


def main():
    """관리 작업 실행."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django를 가져올 수 없습니다. 설치되었는지 확인하고 "
            "PYTHONPATH 환경 변수에서 사용할 수 있습니까? 당신은 "
            "가상 환경을 활성화하는 것을 잊으십시오?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
