from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
)
from django.shortcuts import render
from .models import Post, Category, Product
from django.core.paginator import Paginator


class HomePageView(TemplateView):
    template_name = 'index.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ServicePageView(TemplateView):
    template_name = 'service.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class BlogPageView(ListView):
    model = Post
    template_name = 'blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    # search code
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = products.filter(name__icontains=item_name)

    # paginator code
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    return render(
        request,
        'list.html',
        {
            'categories': categories,
            'products': products
        }
    )


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', {'product': product})
