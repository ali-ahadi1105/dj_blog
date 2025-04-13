from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "بلاگ خودمونی طور"

@register.inclusion_tag('blog/partials/navbar.html')
def navbar():
    return {
        "categories": Category.objects.filter(status=True)
    }