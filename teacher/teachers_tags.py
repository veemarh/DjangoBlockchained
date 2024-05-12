from django import template
from django.utils.http import urlencode

from .models import Categories

register = template.Library()


@register.simple_tag
def tag_categories():
    return Categories.objects.all()


# Для того, чтобы следующие страницы при фильтрации имели такой же фильтр, как и на первой
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
