from .models import Comment, Product
from django import forms
from .models import *
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('content', )

class RegisterForm(forms.Form):
    CATEGORIES = [
        ('의류', '의류'),
        ('여행', '여행'),
        ('화장품', '화장품'),
        ('가구', '가구'),
        ('식품', '식품'),

        # 다른 카테고리도 필요에 따라 추가할 수 있습니다
    ]

    name = forms.CharField(
        error_messages={'required':"상품명을 입력하세요."},
        max_length=32, label="상품명"
    )

    price = forms.IntegerField(
        error_messages={'required': "가격을 입력하세요."},
        label="가격"
    )

    stock = forms.IntegerField(
        error_messages={'required': "수량을 입력하세요"},
        label="재고"
    )

    description = forms.CharField(
        error_messages={'required': "상품 설명을 입력하세요"},
        label="상품 설명"
    )

    category = forms.ChoiceField(
        choices=CATEGORIES,
        error_messages={'required': "카테고리를 선택하세요"},
        label="카테고리"
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        category = cleaned_data.get('category')
        price = cleaned_data.get('price')
        stock = cleaned_data.get('stock')
        description = cleaned_data.get('description')

        if not (name and category and price and stock and description):
            self.add_error(None, "값이 없습니다.")
