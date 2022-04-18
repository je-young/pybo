from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modipy_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인 추가


    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modipy_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


# filter에 대한 자세한 사용법은 장고 공식 문서
# 참고 : https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types

# Making queries에 대한 자세한 사용법은 장고 공식 문서
# 참고 : https://docs.djangoproject.com/en/4.0/topics/db/queries/

# 모델 변경후 makemigrations 명령과 migrate 명령을 실행