from django.db import models
from faker import Faker
f = Faker()

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    # VARCHAR(100) 랑 대응되어서 max_length 써주는 것임
    keyword = models.CharField(max_length=50)
    email = models.CharField(max_length = 200)
    content = models.TextField()
    
    date = models.DateField(blank = True, null = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    # blank = True 
    # null = True 

    # 3번의 validating 검사할 기회
    # 1. HTML에서 required, min_length 등 1차적으로 방어(검사)

    # 2. django form의 is_valid(), 거의 여기서 걸러짐

    # 3. DB, is_valid 통과했지만 save할 때 안 받아질 때, INSERT INTO 할때 제약 조건에서 걸러질 때

    # null=True는 DB에서 통과 시켜줌 , 마지막 단계 방화벽 없애줌
    # blank = True 2번 통과시켜줌, 2번째 단계 방화벽 없애줌

    # 예외 케이스 Char, TextField / blank만 줘도 된다. 통과시 null이 아니라 빈 스트링('') 으로 넘겨줘서
    # 빈 스트링은 NULL이 아니라 통과시켜줌

    
    @classmethod
    def dummy(cls, n):
        # article = cls()
        # article.title = 이런 거랑 같음
        for i in range(n):
            cls.objects.create(
                title=f.text(20),
                content=f.text(),
                keyword=f.company(),
                email=f.email(),
            )

class Comment(models.Model):
    content = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)