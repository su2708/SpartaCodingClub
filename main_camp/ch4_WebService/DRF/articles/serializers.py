from rest_framework import serializers
from .models import Article, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret


class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    # comments_count는 직접 필드를 추가해 주는 것(Django가 알아서 추가해주는 것이 아님!)
    # source 속성을 이용하여 데이터 값을 전달
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)
    
    class Meta:
        model = Article
        fields = "__all__"


class ArticleDetailSerializer(ArticleSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.IntegerField(source="comments.count", read_only=True)