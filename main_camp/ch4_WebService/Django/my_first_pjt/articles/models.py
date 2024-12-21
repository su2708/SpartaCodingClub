from django.db import models


# Create your models here.
# 작성하는 글에 대한 모델 
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="images/",
        blank=True  # 이미지가 없어도 괜찮다는 의미 
    )

    def __str__(self):
        return self.title

# 작성하는 댓글에 대한 모델
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  # Article이 사라지면 이 댓글도 삭제된다는 옵션
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content