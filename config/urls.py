"""구성 URL 구성

'urlpatterns' 목록은 URL을 보기로 라우팅합니다. 자세한 내용은 다음을 참조하십시오.:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. 가져오기 추가: my_app 가져오기 보기에서
    2. urlpatterns에 URL 추가:  path('', views.home, name='home')
Class-based views
    1. 가져오기 추가:  from other_app.views import Home
    2. urlpatterns에 URL 추가:  path('', Home.as_view(), name='home')
Including another URLconf
    1. include() 함수 가져오기: from django.urls import include, path
    2. urlpatterns에 URL 추가:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementTree import fromstring
from django.contrib import admin
from django.urls import path, include
from pybo.views import base_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'), # '/' 에 해당되는 path

]
