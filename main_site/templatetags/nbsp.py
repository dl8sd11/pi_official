from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def nbsp(value):
    space_str = "&nbsp;".join(value.split(' '))
    return mark_safe("<br>".join(space_str.split('\n')))