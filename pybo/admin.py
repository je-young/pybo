from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)
# admin.site.register로 Question 모델을 등록했다. 그리고 장고 관리자 화면을 갱신해 보면 다음처럼 Question이 추가된 것을 확인할 수 있다.
# Question 모델에 세부 기능을 추가할 수 있는 QuestionAdmin 클래스를 생성하고 제목 검색을 위해 search_fields 속성에 'subject'를 추가

# 장고관리자 공식문서 참고
# https://docs.djangoproject.com/en/4.0/ref/contrib/admin/

# Register your models here.
