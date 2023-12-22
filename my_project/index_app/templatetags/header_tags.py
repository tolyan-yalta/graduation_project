from django import template
from index_app.menu import menu

register = template.Library()

@register.simple_tag
def get_menu():
    return menu