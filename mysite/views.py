from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404,render, redirect
from django.contrib.auth.decorators import login_required
from .models import MainContent, Comment ,Product,Category
from .forms import CommentForm, RegisterForm
from django.views.generic.edit import FormView
from django.utils.decorators import *
from django.views.generic import ListView


# Create your views here.
def index(request):
    content_list = Product.objects.order_by('registered_date')
    context ={ 'content_list':content_list}
    return render(request, 'mysite/content_list.html' , context)

def detail(request, content_id):
 content_list = Product.objects.get(id=content_id)
 context = { 'content_list': content_list}
 return render(request, 'mysite/content_detail.html', context)

def comment_create(request, content_id):
    content_list = get_object_or_404(MainContent,pk=content_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.content_list= content_list
            comment.author = request.user
            comment.save()
            return redirect('detail', content_id = content_list.id)
    else:
        form = CommentForm()
    context = {'content_list':content_list , 'form':form}
    return render(request ,'mysite/content_detail.html',context)


@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
        raise PermissionDenied

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('detail', content_id=comment.content_list.id)
    else:
        form = CommentForm(instance=comment)
        
    context = {'comment': comment, 'form': form}
    return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.user != comment.author:
         raise PermissionDenied
    else:
        comment.delete()
    return redirect('detail', content_id=comment.content_list.id)

class ProductRegister(FormView):
    template_name = 'mysite/product_register.html'
    form_class = RegisterForm
    success_url = '/mysite/'


    def form_valid(self, form):
        name = form.cleaned_data['name']
        category_name = form.cleaned_data['category']  # Get the category name from the form

        # Try to get the existing category with the given name
        category_instance = Category.objects.filter(name=category_name).first()

        if category_instance is None:
            # If the category doesn't exist, create a new one
            category_instance = Category.objects.create(name=category_name)

        price = form.cleaned_data['price']
        stock = form.cleaned_data['stock']
        description = form.cleaned_data['description']
        imgfile = self.request.FILES.get('imgfile')  # Get the uploaded image file

        product = Product(
            name=name,
            category=category_instance,
            price=price,
            stock=stock,
            description=description,
            imgfile=imgfile
        )
        product.save()
        return super().form_valid(form)

class CategoryView(ListView):
    model = Category  # 모델에 맞게 수정해야 합니다.
    template_name = 'category_list.html'  # 카테고리 목록을 나타낼 템플릿
    context_object_name = 'categories'  # 템플릿에서 사용할 컨텍스트 변수명

def category_detail(request, category_id):
    # 카테고리 객체 가져오기
    category = get_object_or_404(Category, pk=category_id)

    # 카테고리에 속한 상품들 가져오기
    products = Product.objects.filter(category=category)

    # 기타 필요한 로직 수행...

    return render(request, 'mysite/category_detail.html', {'category': category, 'products': products})