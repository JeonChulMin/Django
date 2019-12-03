from django.shortcuts import render, get_object_or_404, redirect
# get_list_or_404는 안씀, DB에 데이터에 하나도 없을 때 사용자가 페이지에 접근하지 못하는 이슈가 발생할 수 있어 잘 안씀
from .models import Article, Comment
from .forms import ArticleForm


# Create your views here.
def new_article(request):
    if request.method == 'POST':
        # 사용자가 데이터를 제출한 시점
        form = ArticleForm(request.POST)
        # 알아서 각 컬럼에 데이터들이 찾아서 들어감
                
        # print('Data 넘어옴')

        # 이상한 데이터를 걸러내는게 포인트
        if form.is_valid():
            # 넘어온 데이터들 다 유효해?라고 물어봄
            article = form.save()
            return redirect('board:article_detail', article.id)
        
    # a = Article()
    # a.title = request.POST.get('title')
    # 이런식으로 안써줘도 된다.
    else :
        # GET
        
        form = ArticleForm()

    context = {
        'form': form,
    }
    # print(f'Data {form.errors}')
    return render(request, 'board/article_form.html', context)

def article_list(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'board/article_list.html', context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 특정 하나만 찾을 경우 사용한다. get_object_or_404
    context = {
        'article':article
    }
    return render(request, 'board/article_detail.html', context)

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    # 있는지 없는지 판단해줌, 먼저 가져와야 되니까 맨 처음 실행

    if request.method == 'POST':
        # 사용자가 데이터를 제출한 시점
        form = ArticleForm(request.POST, instance=article)
        # instance=article를 수정하겠다.
        # 알아서 각 컬럼에 데이터들이 찾아서 들어감

        # 이상한 데이터를 걸러내는게 포인트
        if form.is_valid():
            # 넘어온 데이터들 다 유효해?라고 물어봄
            article = form.save()
            return redirect('board:article_detail', article.id)
        
    # a = Article()
    # a.title = request.POST.get('title')
    # 이런식으로 안써줘도 된다.
    else :
        # GET
        form = ArticleForm(instance=article)

    context = {
        'form': form,
    }
    return render(request, 'board/article_form.html', context)