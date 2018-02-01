from django.http import HttpResponse
from django.shortcuts import render, redirect
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

    # posts = Post.objects.all().order_by('-created_date')
    # posts = Post.objects.order_by('-created_date')
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

def post_edit(request, pk):
    """
    pk에 해당하는 Post인스턴스를
    context라는 dict에 'post'키에 할당
    위에서 생성한 dict는 render의 context에 전달

    사용하는 템플릿은 'blog/post_add.html'

    url은 /3/edit/ <- 에 매칭되도록 urls.py에 작성
    :param request:
    :param pk:
    :return:
    """
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
    }
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        if title and content:
            post.title = title
            post.content = content
            post.save()
            return redirect('post-detail', pk=post.pk)
        context['form_error'] = "제목과 내용을 입력하세요"
    return render(request, 'blog/post_add_edit.html', context)



def post_add(request):
    # localhost:8000/ 접근시
    # 이 뷰가 실행되어서 Post add page라는 문구가 보여주도록 urls 작성
    # HttpResponse가 아니라 blog/post_add.html을 출력
    # post_add.html은 base.html을 확장, title(h2)부분에 'Post add'라고 출력

    # return HttpResponse('Post add page!')
    context = {

    }
    if request.method == "POST":
        # 요청의 method가 POST일 때
        # HttpResponse로 POST요청에 담겨온
        # title과 content를 합친 문자열 데이터를 보여줌
        title = request.POST['title']
        content = request.POST['content']

        # title이나 content가 비어있으면
        # 다시 글 작성화면으로 이동
        if title and content:
            post = Post.objects.create(
                author=request.user,
                title=title,
                content=content,
            )
            # post-detail이라는 URL name을 가진 뷰로
            # 리디렉션 요청을 보냄
            # 이 때, post-detail URL name으로 특정 URL을 만드려면
            # pk값이 필요하므로 키워드 인수로 해당 값을 넘겨준다
            return redirect('post-detail', pk=post.pk)
            # return redirect('post-add')

            # ORM을 사용해서 title과 content에 해당하는
            # post-detail이라는 URL name을 가진 뷰로
            # 리디렉션 요청을 보냄
            # 이 때, post-detail URL name으로 특정 URL을 만드려면
            # pk값이 필요하므로 키워드 인수로 해당 값을 넘겨준다
            # return HttpResponse(f'{post.pk}, {post.title}. {post.content}')

            # 만약 redirect가 아닌 render를 사용할 경우
            # context = {
            #     'post': post,
            # }
            # return render(request, 'blog/post_detail.html', context)

            # 1. post_add페이지를 보여줌 (GET)
            # 2. post_add페이지에서 글 작성 (POST요청)
            # 3. post_add view에서 POST요청에 대한 처리 완료후, 브라우저에는 post-detail(pk=...)에 해당하는 주소로
            # redirect를 하도록 응답 (301 redirect, URL: /3)
            # 4. 브라우저는 301 redirect코드를 갖는 HTTP response를 받고, 해당 URL로 GET 요청을 보냄
            # 5. '/3'주소로 온 요청은 다시 runserver -> Django코드 -> config/urls.py -> blog/urls.py
            # -> def post_detail(request, pk)로 도착, post_detail뷰 처리가 완료된 post_detail.html의 내용을 응답
            # -> 브라우저는 해당 내용을 보여줌
    # else:
        context['form_error'] = "제목이나 내용을 입력해주세요."
    #     # 요청의 method가 GET일 때
    #     return render(request, 'blog/post_add_edit.html')
    return render(request, 'blog/post_add_edit.html', context)

def post_delete(request, pk):
    """
    post_detail의 구조를 참조해서
    pk에 해당하는 post를 삭제하는 view를 구현하고 url과 연결

    삭제코드
        post = Post.objects.get(pk=pk)
        post.delete()

    """
    if request.method == "POST":
        post = Post.objects.get(pk=pk)
        if request.user == post.author:
            post.delete()
            return redirect('post-list')
        return redirect('post-detail', pk=post.pk)