from django.urls import path, re_path
#from blog import views
from . import views

urlpatterns = [
    path('', views.post_list),
    # 3/
    # 53/
    # 53/asdf/ <- X
    re_path(r'(?P<pk>\d*)/$', views.post_detail),
    # 숫자가 1개이상 반복되는 경우를 정규표현식으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
]
