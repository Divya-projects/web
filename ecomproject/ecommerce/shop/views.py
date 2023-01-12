from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.
# def index(request):
#     return HttpResponse('Hey am here')

def allProdCat(request,c_slug=None):
    c_page=None
    products_list=None
    print(f'slugggggggg {c_slug}')
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        print(f'pageeeeeee {c_page}')
        products_list=Product.objects.all().filter(category=c_page, available=True)
    else:
        products_list=Product.objects.all().filter(available=True)

    paginator = Paginator(products_list, 6)
    print(f'paginatorrrrrrrrrrrrrrrrr {paginator}')

    try:
        page=int(request.GET.get('page','1'))
        print(f'in tryyyyyyyyyyyyyyyyyy page {page}')

    except:
        page=1
    try:
        products=paginator.page(page)
        print(f'in tryyyy2222222222 products {products}')
        print(f'pageeeeee number {paginator.num_pages}')
    except(EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products})

def proDetail(request,c_slug,prod_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=prod_slug)
    except Exception as e:
        print(f'')
        raise e
    return render(request,'productdetail.html',{'product':product})


