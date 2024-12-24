from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()  # 현재 활성화된 user model인 User를 model로 사용 
        fields = UserCreationForm.Meta.fields + ()