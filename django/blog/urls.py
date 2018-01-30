from django.urls import path, re_path
#from blog import views
from . import views

urlpatterns = [
    path('list', views.post_list, name='post-list'),
    # 3/
    # 53/
    # 53/asdf/ <- X
    # re_path(r'(?P<pk>\d+)/$', views.post_detail),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    # 숫자가 1개이상 반복되는 경우를 정규표현식으로 구현하되
    # 해당 반복구간을 그룹으로 묶고, 그룹 이름을 'pk'로 지정
]
# URL:      localhost:8000/post/3/
# Path:     post/<int:pk>/
# URL name: post-detail
#                 kwargs: {'pk': <int value>}
#
# ---거꾸로---
# URL name: post-list
# Path:     list
# URL:      localhost:8000/list
#
# --거꾸로(post-detail)---
# URL name: post-detail
#           kwargs: {pk: <int value>}
# Path:     post/<int:pk>/
# URL:      localhost:8000/post/<int value>/