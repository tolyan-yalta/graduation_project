from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product, Category
from basket_app.forms import BasketAddProductForm
from django.core.paginator import Paginator
# from django.urls import reverse


# def catalog(request):
#     """Выводит все товары"""
#     # html = """
#     # <h1>Страница каталога.</h1>
#     # <p>Это страница каталога проекта.</p>
#     # """
#     # logger.info("The catalog page has been uploaded.")
#     products = Product.objects.all()
    
#     data = {
#         # 'title': f'Рубрика: {category.name}',
#         # 'title': f'{category.name}',
#         # 'menu': menu,
#         'products': products,
#         # 'basket_product_form': basket_product_form,
#         # 'cat_selected': category.pk,
#     }
#     return render(request, 'catalog_app/catalog.html', context=data)
#     # return HttpResponse(html)

# def catalog(request):
#     """Выводит все товары"""
#     products = Product.objects.all()
#     paginator = Paginator(products, 12)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     # data = {'products': products,}
#     # return render(request, 'catalog_app/catalog.html', context=data)
#     return render(request, 'catalog_app/catalog.html', {'page_obj': page_obj})


# def show_category(request, cat_slug):
#     """Выводит товары выбранной категории"""
#     category = get_object_or_404(Category, slug=cat_slug)
#     products = Product.objects.filter(category_id=category.pk)
#     paginator = Paginator(products, 12)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     data = {'title': f'{category.name}',
#         # 'products': products,
#         'page_obj': page_obj,
#         'cat_selected': category.pk,}
#     return render(request, 'catalog_app/catalog.html', context=data)


def catalog(request):
    return HttpResponseRedirect('/catalog/products/all')

def products(request, cat_slug=None):
    """Выводит товары"""
    if cat_slug == "all":
        products = Product.objects.all()
        title = "all"
        cat_selected = None
    else:
        category = get_object_or_404(Category, slug=cat_slug)
        products = Product.objects.filter(category_id=category.pk)
        title = category.name
        cat_selected = category.pk

    page_number = request.GET.get('page', 1)
    order_by = request.GET.get('order_by', None)

    if order_by and order_by != "default":
        products = products.order_by(order_by)

    paginator = Paginator(products, 12)
    page_obj = paginator.get_page(page_number)
    data = {'title': title,
            'page_obj': page_obj,
            'cat_selected': cat_selected,
            }

    return render(request, 'catalog_app/catalog.html', context=data)


def product_detail(request, id, slug):
    """Выводит выбранный товар"""
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    category_name = product.category.name
    basket_product_form = BasketAddProductForm()
    return render(request, 'catalog_app/product_detail.html',
                  {'product': product, 
                   'category_name': category_name,
                   'basket_product_form': basket_product_form})
