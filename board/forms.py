from django import forms
# from django.db import models
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(min_length=2, strip=True)
    # strip은 좌우에있는 스페이스 엔터 날려줌
    email = forms.EmailField()
    keyword = forms.CharField(min_length=1, max_length=10)
    
    class Meta:
        model = Article
        exclude = ['date',]
        #fields ='__all__'
    # Meta 안 변수들은 다 이름 맞춰줘야 함
    # all이 변수 전부다 를 뜻
    # 전부다 안쓰고 싶을 때 튜플 이용해서 표현
    #fiedls = ('title', 'content'), 쓰고자 하는 것들만 나옴, 검증도 이것들만 함

    # 하나 뺴고 다 쓰고 싶을 떄
    # exclude = ('date')
    

    # title = ''
    # content = ''
    # email = ''
    # keyword = ''
    # date = ''

    # 다시 똑같은 이유로 다시 정의