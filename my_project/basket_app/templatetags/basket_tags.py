from django import template
# from catalog_app.models import Category
from basket_app.forms import BasketAddProductForm

register = template.Library()


@register.simple_tag()
def basket_product_form():
    form = BasketAddProductForm()
    return form
