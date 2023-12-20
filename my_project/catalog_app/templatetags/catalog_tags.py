from django import template
import catalog_app.views as views
from catalog_app.models import Category
from index_app.menu import menu

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     return views.categories_db


@register.inclusion_tag('catalog_app/list_categories.html')
def show_categories(cat_selected=0):
# def show_categories():
    categories = Category.objects.all()
    # categories = views.categories_db
    return {'categories': categories, 'cat_selected': cat_selected}
    # return {'categories': categories}

# @register.simple_tag()
# def get_absolute_url_tag(cat):
#     return Category.get_absolute_url(cat)

@register.simple_tag
def get_menu():
    return menu
