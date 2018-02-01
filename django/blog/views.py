from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    # 1. 브라우저에서 요청
    # 2. 요청이 runserver로 실행 중인 서버에 도착
    #   2.1. admin/인 경우 admin.site.urls로 전달
    # 3. runserver는 요청을 Django code로 전달
    # 4. DJango code 중 config.urls모듈이 해당 요청을 받음
    # 5. config.urls모듈은 ''(admin/를 제외한 모든 요청)을 blog.urls모듈로 전달
    # 6. blog.urls모듈은 받은 요청의 URL과 일치하는 패턴이 있는지 검사
    # 7. 있다면 일치하는 패턴과 연결된 함수(view)를 실행
    #   7.1. settings모듈의 TEMPLATES속성 내의 DIRS목록에서 blog/post_list.html파일의 내용을 가저옴
    #   7.2. 가져온 내용을 적절히 처리(렌더링, render()함수)하여 리턴
    # 8. 함수의 실행 결과(리턴값)를 브라우저로 다시 전달

    # HTTP프로토콜로 텍스트 데이터 응답을 반환
    # return HttpResponse('<html><body><h1>Post list</h1><p>Post목록을 보여줄 예정입니다</p></body></html>')

    posts = Post.objects.all()
    # render()함수에 전달한 dict객체 생성
    context = {
        'posts': posts,
    }
    return render(
        request=request,
        template_name='blog/post_list.html',
        context=context,
    )
    # 위 return코드와 같음
    # return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context)

def post_add(request):
    # localhost:8000/ 접근시
    # 이 뷰가 실행되어서 Post add page라는 문구가 보여주도록 urls 작성
    # HttpResponse가 아니라 blog/post_add.html을 출력
    # post_add.html은 base.html을 확장, title(h2)부분에 'Post add'라고 출력

    # return HttpResponse('Post add page!')
    return render(request, 'blog/post_add.html')