from django import forms
from articles.models import Article, Comment


class ArticleForm(forms.ModelForm):
    # '어떤 모델을 가져와서 Form을 만들어야 하는가?'를 Meta class에 정의
    class Meta:
        model = Article  # 가져올 model
        fields = "__all__"  # model에서 가져올 속성들
        exclude = ("author", "like_users")  # fields로 가져온 속성들 중에서 제외할 것들

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude = ("article", "user")