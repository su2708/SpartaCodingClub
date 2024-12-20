from django.db import models


# Create your models here.
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
